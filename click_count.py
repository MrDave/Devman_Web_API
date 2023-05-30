import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


load_dotenv()
token = os.getenv("BIT_TOKEN")


def shorten_link(token, long_url):
    link_test = requests.get(long_url)
    link_test.raise_for_status()

    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {
        "long_url": long_url,
        "domain": "bit.ly",
        "group_guid": "Bm46cGtZa0J"
    }

    r = requests.post(url, headers=headers, json=data)
    r.raise_for_status()

    return r.json()["link"]


def count_clicks(token, bitlink):

    link_test = requests.get(bitlink)
    link_test.raise_for_status()

    p = urlparse(bitlink)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{p.netloc + p.path}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = (
        ("unit", "day"),
        ("units", "-1"),
    )

    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    
    return r.json()["total_clicks"]


def is_bitlink(url):

    p = urlparse(url)
    if p.netloc == "bit.ly":
        return True
    else:
        return False


def main():
    user_link = input("Enter your link: ")
    try:
        if is_bitlink(user_link):
            result = count_clicks(token=token, bitlink=user_link)
            print(f"The link is a bitlink and was clicked exactly {result} time(s)")

        else:
            result = shorten_link(token=token, long_url=user_link)
            print(f"Your link wasn't a bitlink, but now it is!\nHere is it: {result}")

    except requests.exceptions.HTTPError as error:
        exit(f"Invalid link: \n{error}")


if __name__ == "__main__":
    main()
