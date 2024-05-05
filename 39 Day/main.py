# %%
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

import datetime

# USER_NAME = str(input("Enter user name for sheety"))
# PASSWORD = str(input("Enter password for sheety"))
USER_NAME = ""
PASSWORD = ""

API_KEY_FLIGHT_DEALS = ""


ROUTES_TO = ["PAR", "BER", "BCN", "PMI", "LON"]
ROUTES_FROM = ["STR" for val in range(len(ROUTES_TO))]

if __name__ == "__main__":
    next_week = datetime.datetime.now()
    next_week = next_week + datetime.timedelta(days=1)
    next_week_formatted = f"{next_week.day}/{next_week.month}/{next_week.year}"
    
    delta_days = next_week + datetime.timedelta(days=6*30)
    next_next_weeks_formatted = f"{delta_days.day}/{delta_days.month}/{delta_days.year}"


    for r_from, r_to in zip(ROUTES_FROM, ROUTES_TO):

        fsearch = FlightSearch(flight_from=r_from, flight_to=r_to, 
                            date_from=next_week_formatted, date_to=next_next_weeks_formatted,
                            apikey="", 
                            api_endpoint="https://api.tequila.kiwi.com/v2/search")
        
        response_sheety_ready = fsearch.search_for_flights()

        d_manager = DataManager(user_name=USER_NAME, user_password=PASSWORD, json_to_sheety=response_sheety_ready, api_endpoint="")

        fsearch.flight_data
    
