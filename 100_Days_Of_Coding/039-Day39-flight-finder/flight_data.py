import datetime as dt

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flight_data) -> None:
        self.price = flight_data['price']
        self.origin_city = flight_data['cityFrom']
        self.origin_airport = flight_data['flyFrom']
        self.destination_city = flight_data['cityTo']
        self.destination_airport = flight_data['flyTo']
        self.out_date = dt.datetime.fromtimestamp(flight_data["route"][0]['dTime']).strftime("%d/%m/%Y")
        self.return_date = dt.datetime.fromtimestamp(flight_data["route"][1]['aTime']).strftime("%d/%m/%Y")
        