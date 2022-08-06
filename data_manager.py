import requests
import os

#manages the data within google sheets
    #needs to be able to input iata codes from the flight api
class DataManager:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.auth_code = os.environ.get("SHEETY_AUTH_CODE")
        self.headers= {
            "Authorization": "Bearer " + self.auth_code
        }
        
        pass

    def get_data(self) -> dict:
        self.response = requests.get(url=self.endpoint, headers=self.headers)
        return self.response.json()
    
    #input iata codes based on the airport/city
    def add_data(self, **kwargs):
        kwargs = {
            "City":"noname",
            "IATA Code":"n/a",
            "Lowest Price":"n/a",
        }
        row = {
            "price":{
                "city":kwargs["City"],
                "iatacode":kwargs["IATA Code"],
                "lowestPrice":kwargs["Lowest Price"],
            }
        }
        self.response = requests.post(url=self.endpoint, headers=self.headers, json=row)
        pass

    #update existing rows in sheet
    def edit_row(self, city: str):
        pass
    
    def update_data(self):
        self.response = requests.get(url=self.endpoint, headers=self.headers)
        self.data = self.response.json()
        pass
    pass