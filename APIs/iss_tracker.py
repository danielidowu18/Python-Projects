import requests
import datetime as dt
import smtplib
import time

my_lat = 6.524376
my_long = 3.379206
my_email = "jidog.100@gmail.com"
password = "yqjyxqifhsrkiyne"

now = dt.datetime.now()
current_hour = now.hour

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0,
}


with requests.get(url="https://api.open-notify.org/iss-now.json") as iss_response:
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_lat = float(iss_data["iss-position"]["latitude"])
    iss_long = float(iss_data["iss-position"]["longitude"])


with requests.get(url="https://api.sunrise-sunset.org/json", params=parameters) as response:
    response.raise_for_status()
    data = response.json()
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    
while True:
    time.sleep(60)
    if -5 <= iss_lat - my_lat <= 5 and -5 <= iss_long - my_long <= 5 and (sunset_hour <= current_hour or current_hour <= sunrise_hour):
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:ISS around you\n\nLook up.")
    
    