import requests
import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv("BIT_TOKEN")
url = "https://api-ssl.bitly.com/v4/user"
headers = {
    "Authorization": f"Bearer {token}"
}
r = requests.get(url, headers=headers)
r.raise_for_status()

print(r.json())
