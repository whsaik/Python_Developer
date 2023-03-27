import datetime as dt

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flight_data, max_stopovers=0) -> None:
        self.price = flight_data['price']
        self.origin_city = flight_data['cityFrom']
        self.origin_airport = flight_data['flyFrom']
        self.destination_city = flight_data['cityTo']
        self.destination_airport = flight_data['flyTo']
        self.stop_over = max_stopovers
        self.out_date = dt.datetime.fromtimestamp(flight_data["route"][0]['dTime']).strftime("%Y-%m-%d")
        self.return_date = dt.datetime.fromtimestamp(flight_data["route"][1]['aTime']).strftime("%Y-%m-%d")
        self.route = [(stop['cityFrom'], stop['flyFrom'], \
            stop['cityTo'], stop['flyTo']) for stop in flight_data["route"]]