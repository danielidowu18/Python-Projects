import requests
# from twilio.rest import client

my_lat = 6.524376
my_long = 3.379206
my_appid = "a52ff5b6f2f88d40bda426833eb556ad"

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": my_appid,
}


with requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters) as response:
    response.raise_for_status()
    data = response.json()
    
new_data = data["list"][0:5]
for item in new_data:
    if item["weather"][0]["id"] < 700:
        print("Bring an Umbrella")
        break
    
    # print(data)