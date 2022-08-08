import sys
import requests
import os
import pandas as pd
from flight_search import FlightSearch 

SHEETY_ENDPOINT = "https://api.sheety.co/1db8be9d672ce7fb4dda78c9c9791eb9/dataFlightDeals/prices"
SHEETY_AUTH_CODE = os.environ.get("SHEETY_AUTH_CODE")
#manages the data within google sheets
    #needs to be able to input iata codes from the flight api
class DataManager:
    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.headers= {
            "Authorization": "Bearer " + SHEETY_AUTH_CODE
        }
        
        pass

    def get_data(self) -> dict:
        self.response = requests.get(url=self.endpoint, headers=self.headers)
        return self.response.json()
    
    #add a new row, takes city as input
    ##from city input, will find iata code and price from flight data
    def add_data(self, city: str, iata_code: str, max_price=sys.maxsize):
        row = {
            "price":{
                "city":city,
                "iataCode":iata_code,
                "lowestPrice":"",
                "maxPrice":max_price
            }
        }
        self.response = requests.post(url=self.endpoint, headers=self.headers, json=row)
        pass
    
    #update price by row
    def update_row_price(self, row_id: int, price: int):
        row_endpoint = self.endpoint + f"/{row_id}"
        data = {
            "price":{
                "lowestPrice":str(price)
            }
        }
        self.response = requests.put(url=row_endpoint, headers=self.headers, json=data)
        pass
    
    


    pass