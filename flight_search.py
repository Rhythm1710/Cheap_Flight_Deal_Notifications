import requests
from flight_data import FlightData

api_key = "Gd5KmEUwoxZUbY28vD0gRSUc9j6qTnE5"
end_point = "https://api.tequila.kiwi.com"


class FlightSearch:
    def get_code(self, city_name):
        location_endpoint = f"{end_point}/locations/query"
        headers = {
            "apikey": "Gd5KmEUwoxZUbY28vD0gRSUc9j6qTnE5"
        }
        parametres = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
        }
        response = requests.get(url=location_endpoint,
                                params=parametres, headers=headers)
        code = response.json()["locations"][0]["id"]
        return code

    def search_flights(self, origin_city_code, destination_airport, from_time, to_time, return_from, return_to):
        headers = {
            "apikey": api_key
        }
        parametres = {
            "fly_from": origin_city_code,
            "fly_to": destination_airport,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "return_to": return_to.strftime("%d/%m/%Y"),
            "return_from": return_from.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(url=f"{end_point}/v2/search", headers=headers, params=parametres)
        try:
            data = response.json()["data"]
            flight_data = FlightData(
                price=data[0]["price"],
                fly_from_city=data[0]["route"][0]["cityFrom"],
                fly_from_airport=data[0]["route"][0]["flyFrom"],
                destination_city=data[0]["route"][0]["cityTo"],
                destination_airport=data[0]["route"][0]["flyTo"],
                out_date=data[0]["route"][0]["local_departure"].split("T")[0],
                return_date=data[0]["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
        except IndexError:
            parametres["max_stopovers"] = 2
            response = requests.get(url=f"{end_point}/v2/search", headers=headers, params=parametres)
            data = response.json()["data"]
            flight_data = FlightData(
                price=data[0]["price"],
                fly_from_city=data[0]["route"][0]["cityFrom"],
                fly_from_airport=data[0]["route"][0]["flyFrom"],
                destination_city=data[1]["route"][0]["cityTo"],
                destination_airport=data[1]["route"][0]["flyTo"],
                out_date=data[0]["route"][0]["local_departure"].split("T")[0],
                return_date=data[0]["route"][3]["local_departure"].split("T")[0],
                via_city=data[0]["route"][0]["cityTo"],
                via_airport=data[0]["route"][0]["flyTo"]
            )
        return flight_data