import smtplib

class NotificationManager:

    def send_mail(self, flight_data):  
        s_mail = "s_mail"
        s_pass = "s_pass"
        r_mail = "r_mail"
        
        text=f"Subject: Low Price Flight Alert!!!\n\nOnly £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport} from {flight_data.out_date} to {flight_data.return_date}."
        text=text.encode("utf-8", "ignore")
    
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=s_mail, password=s_pass)
            connection.sendmail(
                from_addr=s_mail,
                to_addrs=r_mail,
                msg=text
            )
            