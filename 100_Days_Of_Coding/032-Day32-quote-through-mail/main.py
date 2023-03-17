import smtplib
import datetime as dt
import random

DAY_OF_WEEK = ['MONDAY', "TUESDAY", "WEDNESDAY", 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

y_mail = "valaschool@yahoo.com"
g_mail = "happyelaerning0326@gmail.com"
g_pass = "ntalfdlxlpqyudaf"

def send_mail(day, msg_quote, msg_quote_author):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=g_mail, password=g_pass)
        connection.sendmail(
            from_addr=g_mail,
            to_addrs=y_mail,
            msg=f"Subject:Quote of the day - {day}\n\n{msg_quote}\nBy: {msg_quote_author}."
        )

now = dt.datetime.now()
day_of_week = now.weekday()
week_day = DAY_OF_WEEK[day_of_week]
    
with open('quotes.txt', 'r') as file:
    quotes_list = file.readlines()
    quote = random.choice(quotes_list)
    quote_text = quote.split('-')[0].strip()
    quote_author = quote.split('-')[1].strip()

send_mail(week_day, quote_text, quote_author)
