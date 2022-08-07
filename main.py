#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch as fs
from flight_data import FlightData as fd
import json
import pandas



sheet_data = DataManager() 


#add some data to the google sheet first assumes city not in sheet
city_input = "Reno"
start_location = "Los Angeles"
#sheet_data.add_data(city_input, fs.loc_to_iata(city_input))
#sheet_data.add_data("Reno")




flight_data_dict = fs.search_flights(fs.loc_to_iata(start_location), [fs.loc_to_iata(city_input)])
print(flight_data_dict)
price = flight_data_dict[0]["data"][0]["price"]
origin_city = flight_data_dict[0]["data"][0]["route"][0]["cityFrom"]
origin_airport = flight_data_dict[0]["data"][0]["route"][0]["flyFrom"]
destination_city = flight_data_dict[0]["data"][0]["route"][0]["cityTo"]
destination_airport = flight_data_dict[0]["data"][0]["route"][0]["flyTo"]
out_date = flight_data_dict[0]["data"][0]["route"][1]["local_departure"]
return_date = flight_data_dict[0]["data"][0]["route"][1]["local_departure"]

flight_data_list = []
flight_data_list.append(fd(price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date))

#update price after obtaining all flight data
sheet_dict = sheet_data.get_data()
print(sheet_dict)
for (row,info) in zip(sheet_dict["prices"],flight_data_list): 
    sheet_data.update_row_price(row["id"],info.price)