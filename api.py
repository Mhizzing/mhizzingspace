import requests
import os

from dotenv import load_dotenv
from st_helpers import menu_gen

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

    def game_status(self):
        """Get game's status"""
        r = requests.get(self.base_url + '/game/status')
        return r.text

    def system_flight_plans(self, system: str):
        """Get all active flight plans in a system"""
        r = requests.get(self.base_url + f'/game/systems/{system}/flight-plans', headers=self.auth_header)
        return r.text

    def existing_flight_plan(self, flight_plan_id):
        """Get info on an existing flight plan"""
        r = requests.get(self.base_url + f'/users/{self.username}/flight-plans/{flight_plan_id}', headers=self.auth_header)
        return r.text

    def loan_market(self):
        """Get available loans """
        r = requests.get(self.base_url + '/game/loans', headers=self.auth_header)
        return r.text

    def my_loans(self):
        """Get your loans"""
        r = requests.get(self.base_url + f'/users/{self.username}/loans', headers=self.auth_header)
        return r.text, r.url

    def location_info(self, symbol):
        """Get info on a location"""
        r = requests.get(self.base_url + f'/game/locations/{symbol}', headers=self.auth_header)
        return r.text

    def location_ships_info(self, symbol):
        """
        Get info on a location's docked ships
        """
        r = requests.get(self.base_url + f'/game/locations/{symbol}/ships', headers=self.auth_header)
        return r.text

    def system_locations(self, symbol, **kwargs):
        """ 
        Get locations in a system

        kwargs:
            type: type of location you wish to query
        """
        payload = kwargs
        r = requests.get(self.base_url + f'/game/systems/{symbol}/locations', headers=self.auth_header, params=payload)
        return r.text

    def market_info(self, symbol):
        """Get info on a location's marketplace"""
        r = requests.get(self.base_url + f'/game/locations/{symbol}/marketplace', headers = self.auth_header)
        return r.text

    def ship_market(self, **kwargs):
        """
        Get info on available ships
        kwargs:
        class: filter available ships based on class
        """
        payload = kwargs
        r = requests.get(self.base_url + f'/game/ships', headers=self.auth_header, params=payload)
        return r.text

    def my_ship_info(self, ship_id):
        """Get info on a ship you own"""
        r = requests.get(self.base_url + f'/users/{self.username}/ships/{ship_id}', headers=self.auth_header)
        return r.text

    def my_ships(self):
        """Gets a list of your ships"""
        r = requests.get(self.base_url + f'/users/{self.username}/ships', headers=self.auth_header)
        return r.text

    def my_structure_info(self, structure_id):
        """Get info on a structure you own"""
        r = requests.get(self.base_url + f'/users/{self.username}/structures/{structure_id}', headers=self.auth_header)
        return r.text

    def systems_info(self):
        """Get systems info"""
        r = requests.get(self.base_url + '/game/systems', headers=self.auth_header)
        return r.text

    def my_info(self):
        """Get your info"""
        r = requests.get(self.base_url + f'/users/{self.username}', headers=self.auth_header)
        return r.text

class Sender():
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.auth_header = {'Authorization': f'Bearer {self.password}'}

    def new_flight_plan(self):
        """Submit a new flight plan"""
        r = requests.post(self.base_url + f'/users/{self.username}/flight-plans')
        return r.text

    def pay_loan(self, loan_id):
        """Pay off a loan"""
        r = requests.put(self.base_url + f'/users/{self.username}/loans/{loan_id}', headers=self.auth_header)
        return r.text
 
    def request_loan(self, loan_type):
        """Request a new loan"""
        payload = {'type': loan_type}
        r = requests.post(self.base_url + f'/users/{self.username}/loans', headers=self.auth_header, params=payload)
        return r.text

    def purchase_order(self, ship_id, good, quantity):
        """Place a new purchase order"""
        payload = {'shipId': ship_id, 'good': good, 'quantity': quantity}
        r = requests.post(self.base_url + f'/users/{self.username}/purchase-orders', headers=self.auth_header, params=payload)
        return r.text

    def sell_order(self, ship_id, good, quantity):
        """Place a new sell order"""
        payload = {'shipId': ship_id, 'good': good, 'quantity': quantity}
        r = requests.post(self.base_url + f'/users/{self.username}/sell-orders', headers=self.auth_header, params=payload)
        return r.text

    def buy_ship(self, location, ship_type):
        """Buy a new ship"""
        payload = {'location': location, 'type': ship_type}
        r = requests.post(self.base_url + f'/users/{self.username}/ships', headers=self.auth_header, )
        return r.text

    def jettison_cargo(self, ship_id, good, quantity):
        """Jettison's the cargo of a specific ship"""
        payload = {'good': good, 'quantity': quantity}
        r = requests.put(self.base_url + f'/users/{self.username}/ships/{ship_id}/jettison', headers=self.auth_header, params=payload)
        return r.text

    def scrap_ship(self, ship_id):
        """Scrap a ship for credits"""
        r = requests.delete(self.base_url + f'/users/{self.username}/ships/{ship_id}', headers=self.auth_header)
        return r.text

    def ship_cargo_transfer(self, from_ship, to_ship, good, quantity):
        """Transfer cargo frop ship to ship"""
        payload = {'toShipId': to_ship, 'good': good, 'quantity': quantity}
        r = requests.put(self.base_url + f'/users/{self.username}/ships/{to_ship}/transfer', headers=self.auth_header, params=payload)
        return r.text

    def create_structure(self, location, structure_type):
        """Create a new structure"""
        payload = {'location': location, 'type': structure_type}
        r = requests.post(self.base_url + f'/users/{self.username}/structures', headers=self.auth_header, params=payload)
        return r.text

    def structure_deposit(self, structure_id,  ship_id, good, quantity):
        """Deposit goods frop a ship into a structure"""
        payload = {'shipId': ship_id, 'good': good, 'quantity': quantity}
        r = requests.post(self.base_url + f'/users/{self.username}/structures/{structure_id}/deposit', headers=self.auth_header, params=payload)
        return r.text
        
    def structure_cargo_transfer(self, structure_id, ship_id, good, quantity):
        """Transfer cargo from structure to ship"""
        payload = {'shipId': ship_id, 'good': good, 'quantity': quantity}
        r = requests.post(self.base_url + f'/users/{self.username}/structures/{structure_id}/transfer', headers=self.auth_header, params=payload)
        return r.text

def main():
    load_dotenv()

    username = os.environ.get("st_username")
    token = os.environ.get("st_token")
    base_url = 'https://api.spacetraders.io'

    rec = Receiver(base_url, username, token)
    sen = Sender(base_url, username, token)

    q = True

    print(menu_gen(Receiver))
    while q:
        x = input("Initial menu:\n 1. Get information\n 2. Perform an action")
        if x = 1:
            menu_str = menu_gen(Receiver)
            y = input("What would you like to get?\n" + rec_menu)
            if y == 1:
                
            elif y == 2:

            elif y == 3:

            elif y == 4:

            elif y == 5:

            elif y == 6:

            elif y == 7:
                
            elif y == 8:

            elif y == 9:

            elif y == 10:

            elif y == 11:

            elif y == 12:

            elif y == 13:   

            elif y == 14:

            elif y == 15:
  
        elif x = 2:
            menu_str = menu_gen(Sender)
            y = input("What would you like to do?\n" + sen_menu)


if __name__ == "__main__":
    main()