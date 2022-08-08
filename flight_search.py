import os
import requests
import datetime as dt

TEQUILA_ENDPOINT = "http://tequila-api.kiwi.com/"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
headers = {
    "apikey":TEQUILA_API_KEY
}
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    # def __init__(self):
    #     pass
    
    #from and to loc are iata codes
    ##returns flight info of cheapest flight to each location
    def search_flights(from_loc: str, to_loc: list,**kwargs ) -> list:
        from_date=dt.datetime.today().strftime("%d/%m/%Y")
        to_date=((dt.datetime.today() + dt.timedelta(days=30)).strftime("%d/%m/%Y"))
        kwargs={
            "from_date":from_date,
            "to_date":to_date,
        }
        search_endpoint = TEQUILA_ENDPOINT + "v2/search"

        search_results=[]
        for location in to_loc:
            search_params = {
                "fly_from":from_loc,
                "fly_to":location,
                "date_from":kwargs["from_date"],
                "date_to":kwargs["to_date"],
                "one_for_city":"1",
                "curr":"USD",
                "flight_type":"round",
                "nights_in_dst_from":0,
                "nights_in_dst_to":10,
                "max_stopovers":"0"
            }
            response = requests.get(
                url=search_endpoint,
                params=search_params,
                headers=headers
            )
            search_results.append(response.json())
            pass
        return search_results
        pass
    
    #takes in location query like "Los Angeles", returns "LAX"
    def loc_to_iata(loc: str) -> str:
        locations_endpoint = TEQUILA_ENDPOINT  + "locations/query"
        query_params = {
            "term":loc,   
            "location_types":"airport"
        }
        response = requests.get(
                url=locations_endpoint,
                params= query_params,
                headers=headers
            )
        locations_dict = response.json()["locations"]
        iata_code = locations_dict[0]['code']
        return iata_code
        pass

    pass
