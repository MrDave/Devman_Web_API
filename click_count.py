import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse



def shorten_link(token, long_url):
    link_test = requests.get(long_url)
    link_test.raise_for_status()

    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    payload = {
        "long_url": long_url,
    }

    response = requests.post(url, headers, payload)
    response.raise_for_status()

    return response.json()["link"]


def count_clicks(token, bitlink):

    link_test = requests.get(bitlink)
    link_test.raise_for_status()

    parsed = urlparse(bitlink)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc + parsed.path}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = (
        ("unit", "day"),
        ("units", "-1"),
    )

    response = requests.get(url, headers, params)
    response.raise_for_status()
    
    return response.json()["total_clicks"]


def is_bitlink(url):

    parsed = urlparse(url)
    if parsed.netloc == "bit.ly":
        return True
    else:
        return False


def main():

    load_dotenv()
    token = os.getenv("BITLY_AUTH")

    user_link = input("Enter your link: ")
    try:
        if is_bitlink(user_link):
            clicks_total = count_clicks(token, user_link)
            print(f"The link is a bitlink and was clicked exactly {clicks_total} time(s)")

        else:
            short_link = shorten_link(token, user_link)
            print(f"Your link wasn't a bitlink, but now it is!\nHere is it: {short_link}")

    except requests.exceptions.HTTPError as error:
        exit(f"Invalid link: \n{error}")


if __name__ == "__main__":
    main()
