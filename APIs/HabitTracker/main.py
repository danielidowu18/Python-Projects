import requests
from datetime import datetime as dt

username = "jidog"
token = "qwertyasdfzxcv"
graph = "firstgraph"

pixela_endpoint = "https://pixe.la/v1/users"
today = dt.now()
date = today.strftime("%Y%m%d")

header = {
    "X-USER-TOKEN": token,
}

params = {
    "date": date,
    "quantity": input("How many hours did you code today: "),
}

with requests.post(url=f"{pixela_endpoint}/{username}/graphs/{graph}", json=params, headers=header) as response:
    print(response.text)