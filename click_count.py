import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse


def shorten_link(token, long_url):

    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    payload = {
        "long_url": long_url,
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["link"]


def count_clicks(token, bitlink):

    parsed_link = urlparse(bitlink)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}{parsed_link.path}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = (
        ("unit", "day"),
        ("units", "-1"),
    )

    response = requests.get(url, params, headers=headers)
    response.raise_for_status()
    
    return response.json()["total_clicks"]


def is_bitlink(token, link):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    parsed_link = urlparse(link)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}{parsed_link.path}"

    response = requests.get(url, headers=headers)

    return response.ok


def main():

    parser = argparse.ArgumentParser(
        description="Shortens long links and counts total click of short links"
    )
    parser.add_argument("user_link", help="link to shorten or load stats of")
    args = parser.parse_args()

    load_dotenv()
    token = os.environ["BITLY_TOKEN"]

    user_link = args.user_link
    try:
        if is_bitlink(token, user_link):
            clicks_total = count_clicks(token, user_link)
            print(f"The link is a bitlink and was clicked exactly {clicks_total} time(s)")

        else:
            short_link = shorten_link(token, user_link)
            print(f"Your link wasn't a bitlink, but now it is!\nHere is it: {short_link}")

    except requests.exceptions.HTTPError as error:
        raise f"Invalid link: \n{error}"


if __name__ == "__main__":

    main()
