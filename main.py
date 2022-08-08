#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from queue import Empty
from data_manager import DataManager
from flight_search import FlightSearch as fs
from flight_data import FlightData as fd
from notification_manager import NotificationManager 
import json
import pandas


#processes raw flight search data(json) from tequila into FlightData object
def search_to_flight_data(flight_origin_iata: str, flight_destination_iata) -> fd:
    flight_data_dict = fs.search_flights(flight_origin_iata, [flight_destination_iata])
    price = flight_data_dict[0]["data"][0]["price"]
    origin_city = flight_data_dict[0]["data"][0]["route"][0]["cityFrom"]
    origin_airport = flight_data_dict[0]["data"][0]["route"][0]["flyFrom"]
    destination_city = flight_data_dict[0]["data"][0]["route"][0]["cityTo"]
    destination_airport = flight_data_dict[0]["data"][0]["route"][0]["flyTo"]
    out_date = flight_data_dict[0]["data"][0]["route"][0]["local_departure"]
    return_date = flight_data_dict[0]["data"][0]["route"][1]["local_departure"]
    flight_info = fd(price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date)
    return flight_info


sheet_data = DataManager() 

#add some data to the google sheet first assumes city not in sheet
start_location = "Los Angeles"

#eventually allow user to input cities 
city_input = "Reno"
sheet_data.add_data(city_input, fs.loc_to_iata(city_input))


#holds all rows in sheet
sheet_dict = sheet_data.get_data()["prices"]

#read iata from sheet, and generate flight data
flight_data_list = []
for row in sheet_dict:
    flight_data = search_to_flight_data(fs.loc_to_iata(start_location),row["iataCode"])
    flight_data_list.append(flight_data)

#update price after obtaining prices
for (row,info) in zip(sheet_dict,flight_data_list): 
    sheet_data.update_row_price(row["id"],info.price)


#if lowestPrice is less than maxPrice, then send notification via twilio
##sheet_dict
##flight_data_list
###index of each correspond to the same sheet row
flight_notification = ""
sheet_dict = sheet_data.get_data()["prices"]
for (row,flight_info) in zip(sheet_dict,flight_data_list):
    flight_price = row["lowestPrice"]
    max_price = row["maxPrice"]
    if int(flight_price) < max_price:
        flight_notification = flight_notification + flight_info.flight_details()
if(flight_notification != ""):
    NotificationManager.sendNotification(flight_notification)
