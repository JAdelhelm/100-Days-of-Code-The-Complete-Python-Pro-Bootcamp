# %%
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_club import UserClub

import datetime

# USER_NAME = str(input("Enter user name for sheety"))
# PASSWORD = str(input("Enter password for sheety"))
USER_NAME = ""
PASSWORD = ""

API_KEY_FLIGHT_DEALS = ""


ROUTES_TO = ["PAR", "BER", "BCN", "PMI", "LON"]
ROUTES_FROM = ["STR" for val in range(len(ROUTES_TO))]

if __name__ == "__main__":
    today = datetime.datetime.now()
    today_add = today + datetime.timedelta(days=1)
    next_week_formatted = f"{today_add.day}/{today_add.month}/{today_add.year}"
    
    delta_days = today + datetime.timedelta(days=30)
    next_next_weeks_formatted = f"{delta_days.day}/{delta_days.month}/{delta_days.year}"

    # user_club = UserClub(user_name=USER_NAME, 
    #                     user_password=PASSWORD, 
    #                     api_endpoint="")

    for r_from, r_to in zip(ROUTES_FROM, ROUTES_TO):

        fsearch = FlightSearch(flight_from=r_from, flight_to=r_to, 
                            date_from=next_week_formatted, date_to=next_next_weeks_formatted,
                            apikey="", 
                            api_endpoint="https://api.tequila.kiwi.com/v2/search")
        
        response_sheety_ready = fsearch.search_for_flights()

        d_manager = DataManager(user_name=USER_NAME, 
                                user_password=PASSWORD, 
                                json_to_sheety=response_sheety_ready, 
                                api_endpoint="https://api.sheety.co/5d3280a58c1483d800de9673872f2086/flugdeals/flights")

        fsearch.flight_data
    
