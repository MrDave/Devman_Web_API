import requests
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("BIT_TOKEN")
long_url = "https://xkcd.com/178/"


def shorten_link(token, long_url):
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

    print(r.json())


if __name__ == "__main__":
    shorten_link(token=token, long_url=long_url)
