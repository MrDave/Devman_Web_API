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

    results = r.json()
    bitlink = results["link"]

    return bitlink


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


if __name__ == "__main__":
    bitlink = input("Enter full bitlink: ")
    try:
        clicks = count_clicks(token=token, bitlink=bitlink)
    except requests.exceptions.HTTPError as error:
        exit(f"Invalid link: \n{error}")

    print(f"The link was clicked exactly {clicks} time(s)")
