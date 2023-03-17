import smtplib
import random
import datetime as dt
import pandas as pd

#---------------------------- Function to send Mail ----------------------------#
g_mail = "sender_mail"
g_pass = "sender_password"

def send_mail(person):
    # read random letter template
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", 'r') as file:
        letter_text = file.read()
        new_text = letter_text.replace('[NAME]', person['name'])
        
    # sending birthday email    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=g_mail, password=g_pass)
        connection.sendmail(
            from_addr=g_mail,
            to_addrs=person['email'],
            msg=f"Subject: Happy Birthday!\n\n"
            f"{new_text}"
        )
#---------------------------- Birthday Data and Checking ----------------------------# 
now = dt.datetime.now()
month = now.month
day = now.day

data = pd.read_csv("birthdays.csv")
data_list = data.to_dict(orient='records')

# check if there is anyone whose birthday is today
# for person in data_list:
#     if person['month'] == month and person['day'] == day:
#         send_mail(person)

# another way to do...
today = (month, day)

data_dict = {(d_row['month'],d_row['day']):d_row for (index, d_row) in data.iterrows()}
if today in data_dict:
    birthday_person = data_dict[today]
    send_mail(birthday_person)
