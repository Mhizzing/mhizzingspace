import requests
import os

from dotenv import load_dotenv

load_dotenv()
username = os.environ.get('st_username')

r = requests.post(f'https://api.spacetraders.io/users/{username}/token')
print(r.text)