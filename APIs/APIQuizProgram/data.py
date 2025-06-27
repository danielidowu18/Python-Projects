import requests


parameters = {
    "amount": 10,
    "type": "boolean",
}

with requests.get(url="https://opentdb.com/api.php", params=parameters) as response:
    response.raise_for_status()
    question_data = response.json()["results"]
