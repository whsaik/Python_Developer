import requests
from datetime import datetime
import pytz
import smtplib

MY_LAT = 3.415374
MY_LONG = 102.033276

def iss_is_above(lat, long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    # Position is within +5 or -5 degrees of the ISS position.
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5

def send_mail():
    # sending birthday email
    text = "Subject:ISS is near\n\nLook up the sky, ISS is near your location."    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user='sender_mail', password='sender_pass')
        connection.sendmail(
            from_addr='sender_mail',
            to_addrs='receiver_mail',
            msg=text
        )

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    KLTz = pytz.timezone('Asia/Kuala_Lumpur') 
    time_now = datetime.now(KLTz)
    
    return time_now.hour >= sunset or time_now.hour < sunrise

if iss_is_above(MY_LAT, MY_LONG):
    if is_night():
        send_mail()


