class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        pass
    pass

    def flight_details(self) -> str:
        flight_details = f"Flight from {self.origin_city} to {self.destination_city}:\n-price: ${self.price}\n-departure date: {self.out_date}\n-return_date: {self.return_date}\n-airport: {self.origin_airport} -> {self.destination_airport}\n\n"
        return flight_details
        pass