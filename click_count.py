import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


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

    parsed = urlparse(bitlink)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc + parsed.path}/clicks/summary"
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
    parsed = urlparse(link)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc + parsed.path}"

    response = requests.get(url, headers=headers)

    return response.ok


def main():

    load_dotenv()
    token = os.environ["BITLY_TOKEN"]

    user_link = input("Enter your link: ")
    try:
        if is_bitlink(token, user_link):
            clicks_total = count_clicks(token, user_link)
            print(f"The link is a bitlink and was clicked exactly {clicks_total} time(s)")

        else:
            short_link = shorten_link(token, user_link)
            print(f"Your link wasn't a bitlink, but now it is!\nHere is it: {short_link}")

    except requests.exceptions.HTTPError as error:
        exit(f"Invalid link: \n{error}")


if __name__ == "__main__":

    main()

