import requests
import os

from dotenv import load_dotenv

load_dotenv()

# # Game status
# r = requests.get(base_url + '/game/status')
# print(r, r.text)

# # Account / Profile
# r = requests.get(base_url + f'/users/{username}', headers=auth_header)
# print(r, r.text)

# # View available loans
# r = requests.get(base_url + '/game/loans', headers=auth_header)
# print(r, r.text)

# # View ships to purchase
# payload = {'class': 'MK-I'}
# r = requests.get(base_url + '/game/ships', headers=auth_header, params=payload)
# print(r, r.text)

class Receiver():
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.auth_header = {'Authorization': f'Bearer {self.password}'}

    # Get game's status
    def game_status(self):
        r = requests.get(self.base_url + '/game/status')
        return r.text

    # Get all active flight plans in a system
    def system_flight_plans(self, system: str):
        payload = {'symbol': system}
        r = requests.get(self.base_url + '/game/systems/:symbol/flight-plans', headers=self.auth_header, params=payload)
        return r.text

    # Get info on an existing flight plan
    def existing_flight_plan(self, flight_plan_id):
        payload = {'username': self.username, 'flightPlanId': flight_plan_id}
        r = requests.get(self.base_url + '/users/:username/flight-plans/:flightPlanId', headers=self.auth_header, params=payload)
        return r.text

class Sender():
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.auth_header = {'Authorization': f'Bearer {self.password}'}

    # Submit a new flight plan
    def new_flight_plan(self):
        return

def main():
    load_dotenv()

    username = os.environ.get("st_username")
    token = os.environ.get("st_token")
    base_url = 'https://api.spacetraders.io'

    test_rec = Receiver(base_url, username, token)
    print(test_rec.game_status())
    print(test_rec.system_flight_plans('OE-PM-TR'))

if __name__ == "__main__":
    main()