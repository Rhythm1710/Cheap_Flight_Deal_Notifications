
from data_manager import DataManager 
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
from new_user import NewUser


data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
users = data_manager.get_emails()
users_emails = [row["email"] for row in users]
new_user = NewUser()

Origin_city = "LON"

print("Welcome to Rhythm's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your last_name? ")
email = input("What is your email? ")
if input("Type your email again: ")==email and new_user.is_valid_email(email)==True:
    new_user.register_new_user(first_name,last_name,email)
    print("Thank you for signing up.")
else:
    print("Sorry, that's not the same email.")


if sheet_data[0]["iataCode"]=="":
    for row in sheet_data:
        row["iataCode"]=flight_search.get_code(row["city"])
    data_manager.data = sheet_data
    data_manager.update_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
return_date_initial = tomorrow + timedelta(days=7)
return_date_last = six_month_from_today+ timedelta(days=(6*30)+28)

for destination in sheet_data:
    flight = flight_search.search_flights(
        Origin_city,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        return_to=return_date_last,
        return_from=return_date_initial
    )
    if flight.via_airport == "" and flight.price < destination["lowestPrice"]:
        notification_manager.send_msg(
            message=f"LOW PRICE ALERT!! Only £{flight.price} to fly from {flight.fly_from_city}-{flight.fly_from_airport} to {flight.destination_city}-{flight.destination_airport},from {flight.out_date} to {flight.return_date}"
        )
    elif flight.price<destination["lowestPrice"]:
        notification_manager.send_msg(
            message=f"LOW PRICE ALERT!! Only £{flight.price} to fly from {flight.fly_from_city}-{flight.fly_from_airport} to {flight.destination_city}-{flight.destination_airport},from {flight.out_date} to {flight.return_date}.\n\nFlight has 1 stopover, via {flight.via_city}-{flight.via_airport}"
        )

    if flight.via_airport == "" and flight.price < destination["lowestPrice"]:
        message=f"LOW PRICE ALERT!! Only £{flight.price} to fly from {flight.fly_from_city}-{flight.fly_from_airport} to {flight.destination_city}-{flight.destination_airport},from {flight.out_date} to {flight.return_date}"
        
    elif flight.price<destination["lowestPrice"]:
        message=f"LOW PRICE ALERT!! Only £{flight.price} to fly from {flight.fly_from_city}-{flight.fly_from_airport} to {flight.destination_city}-{flight.destination_airport},from {flight.out_date} to {flight.return_date}.\n\nFlight has 1 stopover, via {flight.via_city}-{flight.via_airport}"

    notification_manager.send_emails(users_emails,message)