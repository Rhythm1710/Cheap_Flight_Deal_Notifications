import requests

sheet_endpoint = ""
sheet_headers = {
    "Authorization":"Bearer"
}

class DataManager:
    def __init__(self):
        self.data = {}

    def get_data(self):
        response = requests.get(url=f"{sheet_endpoint}/prices", headers=sheet_headers)
        response.raise_for_status()
        self.data = response.json()["prices"]
        return self.data
    
    def update_data(self):
        for city in self.data:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheet_endpoint}/prices/{city['id']}",json=new_data,headers=sheet_headers)
            print(response.text)
    
    def get_emails(self):
        response = requests.get(url=f"{sheet_endpoint}/users",headers=sheet_headers)
        response.raise_for_status()
        data = response.json()
        self.customers_data = data["users"]
        return self.customers_data

        
