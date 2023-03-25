import requests
import datetime as dt
from flight_data import FlightData

API_KEY = "---"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.         
    def flight_code(self, city):
        endpoint = 'https://api.tequila.kiwi.com/locations/query'
    
        headers = {"apikey": API_KEY}
        
        params = {"term": city}
    
        response = requests.get(url=endpoint, headers=headers, params=params)
        loc_code = response.json()['locations'][0]['code']
        return loc_code
    
    def search_flight(self, departure_airport_code, arrival_airport_code, start_search_date, end_search_date):
        endpoint = 'https://api.tequila.kiwi.com/search'
    
        headers = {"apikey": API_KEY}
        
        params = {
            "fly_from": f'city:{departure_airport_code}',
            "fly_to": f'city:{arrival_airport_code}',
            "date_from": start_search_date,
            "date_to": end_search_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        
        response = requests.get(url=endpoint, headers=headers, params=params)
        data = response.json()['data'][0]
        
        flight_data = FlightData(data)
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
