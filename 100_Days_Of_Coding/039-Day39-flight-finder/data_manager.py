import requests

TOKEN = '---'
        
BEARER_HEADERS = {'Authorization': f'Bearer {TOKEN}'}

class DataManager:
    #This class is responsible for talking to the Google Sheet.    
    def get_destination_data(self):
        sheet_endpoint = 'https://api.sheety.co/---'

        response = requests.get(url=sheet_endpoint, headers=BEARER_HEADERS)
        response.raise_for_status()
        sheet_data = response.json()['prices']
        return sheet_data
        
    def update_flight(self, data):
        sheet_put_api = "https://api.sheety.co/---"
        
        for x in data:
            sheety_data = {
                'price': {
                    'city': x['city'],
                    'iataCode': x['iataCode'],
                    'lowestPrice': x['lowestPrice'],
                }
            }
            
            response = requests.put(url=f"{sheet_put_api}/{x['id']}", json=sheety_data, \
                headers= BEARER_HEADERS)

