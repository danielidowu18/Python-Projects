import requests
# import dotenv

sheet_endpoint = "https://api.sheety.co/e8f44dffe5e5bcc0c28f7d94c2cbfc0e/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, param):
        sheet_param = {
            "iataCode": param,
        }
        self.sheet_response = requests.post(url=sheet_endpoint, params=sheet_param)
        # print(self.sheet_response.text)