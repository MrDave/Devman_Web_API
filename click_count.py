import requests
import os
from dotenv import load_dotenv


def main():

    load_dotenv()
    token = os.getenv("BIT_TOKEN")
    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = """{
        "long_url": "https://xkcd.com/2228",
        "domain": "bit.ly",
        "group_guid": "Bm46cGtZa0J"
    }"""
    r = requests.post(url, headers=headers, data=data)
    r.raise_for_status()

    print(r.json())


if __name__ == "__main__":
    main()
