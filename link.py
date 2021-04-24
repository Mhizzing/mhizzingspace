r.text
import requests
import os

from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("st_username")
token = os.environ.get("st_token")
auth_header = {'Authorization': f'Bearer {token}'}

base_url = 'https://api.spacetraders.io'

# Game status
r = requests.get(base_url + '/game/status')
print(r, r.text)

# Account / Profile
r = requests.get(base_url + f'/users/{username}', headers=auth_header)
print(r, r.text)

# View available loans
r = requests.get(base_url + '/game/loans', headers=auth_header)
print(r, r.text)

# View ships to purchase
payload = {'class': 'MK-I'}
r = requests.get(base_url + '/game/ships', headers=auth_header, params=payload)
print(r, r.text)
