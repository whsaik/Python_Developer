import smtplib

class NotificationManager:

    def send_mail(self, flight_data, customer_data):  
        s_mail = '---'
        s_pass = '---'
        
        # create the route of the journey
        route = ""
        for flight in flight_data.route:
            route += f'{flight[0]}({flight[1]})--{flight[2]}({flight[3]})\n'
                    
        text_content = f"Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport} from {flight_data.out_date} to {flight_data.return_date}."
        flight_link = f"https://www.google.co.uk/travel/flights?hl=en#flt={flight_data.origin_airport}.{flight_data.destination_airport}.{flight_data.out_date}*{flight_data.destination_airport}.{flight_data.origin_airport}.{flight_data.return_date}"
        text=f"Subject: Low Price Flight Alert!!!\n\n{text_content}\nThe route of the flight:\n{route}\n{flight_link}"
        text=text.encode("utf-8")

        for person in customer_data:
            customer_email = person['email']
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=s_mail, password=s_pass)
                connection.sendmail(
                    from_addr=s_mail,
                    to_addrs=customer_email,
                    msg=text
                )
            