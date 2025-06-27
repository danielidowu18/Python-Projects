import requests
from datetime import datetime as dt

APP_ID = "458fb6a4"
API_KEY = "e50010d49d61ab8873e278843b2e192e"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/e8f44dffe5e5bcc0c28f7d94c2cbfc0e/workoutsTracking/workouts"
today = dt.now()
date = today.strftime("%Y/%m/%d")
time = today.strftime("%H:%M:%S")


header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_header = {
    "Authorization": "Basic SmlkX29nOnF3ZXJ0eWFzZGZ6eGN2",
}

param = {
    "query": input("What exercises did you do today?: "),
}

with requests.post(url=nutritionix_endpoint, json=param, headers=header) as response:
    data = response.json()["exercises"]
    for item in data:
        exercise = item["name"].title()
        duration = item["duration_min"]
        calories = item["nf_calories"]
        
        sheety_params = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }
        }
        
        with requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_header) as sheety_response:
            print(sheety_response.text)
