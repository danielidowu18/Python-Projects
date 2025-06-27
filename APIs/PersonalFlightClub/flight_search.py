import requests

tequila_id = "archiepython"
tequila_key = "5YZFEqjGzbcHQuEQRmYyOcsUhBIEVPBA"
tequila_endpoint = "https://api.tequila.kiwi.com/locations/query"

header = {
    "accept": "application/json",
    "apikey": tequila_key,
}

params = {
    "term": "Argentina",
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_response = requests.get(url=tequila_endpoint, params=params, headers=header)
        self.tequila_response.raise_for_status()
        self.data = self.tequila_response.json()["locations"][0]["id"]
        print(self.data)
        
        
        
        
        
        
        


FlightSearch()