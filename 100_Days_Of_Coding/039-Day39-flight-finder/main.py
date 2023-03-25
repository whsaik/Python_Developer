# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager 
# classes to achieve the program requirements.
import datetime as dt
import flight_search as fs
import data_manager as dm
import notification_manager as nm
from pprint import pprint

ORIGINAL_LOC = "LON"

start_search_date = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
end_search_date = (dt.datetime.now() + dt.timedelta(days=(6*30))).strftime("%d/%m/%Y")

sheet_data = dm.DataManager().get_destination_data()

# get the IATA code for the locations
for i in range(len(sheet_data)):
    if sheet_data[i]['iataCode'] == "":
        sheet_data[i]['iataCode'] = fs.FlightSearch().flight_code(sheet_data[i]['city'])

pprint(sheet_data)
    
# update the IATA code
updated_data = dm.DataManager().update_flight(sheet_data)

# check for the cheapest flight for each destination
for destination in sheet_data:
    flight = fs.FlightSearch().search_flight(ORIGINAL_LOC, destination['iataCode'], \
        start_search_date, end_search_date)

    # check whether price is lower
    if float(flight.price) < float(sheet_data[i]['lowestPrice']):
        nm.NotificationManager().send_mail(flight)
        