# %%
import datetime
import requests
from flight_data import FlightData
from data_manager import DataManager

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, flight_from, flight_to, date_from, date_to, apikey, api_endpoint) -> None:
        self.flights_from = flight_from
        self.flights_to = flight_to
        self.date_from = date_from
        self.date_to = date_to
        self.apikey = apikey
        self.api_endpoint = api_endpoint

        self.json_data_flights = None
        self.flight_data = []

        self.parameters = self.set_parameters()
        self.headers = self.set_headers()


    def set_parameters(self):
        return {
            "fly_from": self.flights_from,
            "fly_to": self.flights_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            # Next parameters have to be removed for one-way-flight
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            # "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
    
    def set_headers(self):
        return {
            "apikey": self.apikey
        }

    def search_for_flights(self):
        """
        Parse Data to FlightData Object, which converts the data in a 
        working format for sheety.
        """
        response = requests.get(url=self.api_endpoint, params=self.parameters, headers=self.headers)
        # print("Get Data from API: ", response.status_code)
        try:
            response_in_json = response.json()["data"]
            self.json_data_flights = response_in_json

            # Preprocess Json-Data
            FlightDataPreprocess = FlightData(json_data_flights=self.json_data_flights)
            # formatted_flight_data_topX = FlightDataPreprocess.format_flight_data(return_x_cheapest_flights=3)
            # print("Formatted Reponse: ",formatted_flight_data_topX)
            
            # Send the cheapest flight to DataManager
            formatted_flight_data_top1 = FlightDataPreprocess.format_flight_data(return_x_cheapest_flights=1)
            # print(formatted_flight_data_top1)

            return formatted_flight_data_top1
        
        except Exception as e:
            print(f"No flights found from {self.flights_from} to {self.flights_to}.")
            print(e)
            pass      

          

      

# Check Price from kiwi.com


# if __name__ == "__main__":
#     next_week = datetime.datetime.now()
#     next_week = next_week + datetime.timedelta(days=1)
#     next_week_formatted = f"{next_week.day}/{next_week.month}/{next_week.year}"

#     delta_days = next_week + datetime.timedelta(days=28)
#     next_next_weeks_formatted = f"{delta_days.day}/{delta_days.month}/{delta_days.year}"

#     fsearch = FlightSearch(flight_from="FRA", flight_to="MIA", 
#                            date_from=next_week_formatted, date_to=next_next_weeks_formatted,
#                            apikey="", 
#                            api_endpoint="https://api.tequila.kiwi.com/v2/search")
    
#     response_sheety_ready = fsearch.search_for_flights()

    # fsearch.flight_data