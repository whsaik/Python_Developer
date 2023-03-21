import requests
from twilio.rest import Client
import os

MY_LAT = 3.415374
MY_LONG = 102.033276
API_KEY = os.environ.get('OWM_API_KEY')
API_ENDPOINT = 'https://api.openweathermap.org/data/3.0/onecall'
HOUR_LEN = 12

account_sid = 'AC473cb6ec46d4367230b251db55f89458'
auth_token = os.environ.get('OWN_AUTH_TOKEN')
client = Client(account_sid, auth_token)

weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'exclude': 'current,minutely,daily,alerts',
    'appid': API_KEY,
}

will_rain = False

response = requests.get(url=API_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()["hourly"]
for i in range(HOUR_LEN):
    if int(data[i]['weather'][0]["id"]) < 700:
        will_rain = True
        
if will_rain:
    message = client.messages \
                .create(
                     body="It will be raining soon. Remember to bring an umbrella.☂️",
                     from_='sender_phone_number',
                     to='receiver_phone_number'
                 )
    print(message.status)
