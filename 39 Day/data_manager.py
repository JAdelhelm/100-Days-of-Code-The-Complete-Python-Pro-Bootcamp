import requests
from requests.auth import HTTPBasicAuth

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, user_name, user_password, json_to_sheety, api_endpoint="") -> None:
        self.user_name = user_name
        self.user_password = user_password
        self.api_endpoint = api_endpoint

        self.user_authentication =   HTTPBasicAuth(self.user_name, self.user_password)

        # Get the ceapest flight
        try:
            self.json_to_sheety = json_to_sheety[:1]    
            self.update_flight_prices()
        except:
            pass


    def update_flight_prices(self):

        response = requests.get(url=self.api_endpoint, auth=self.user_authentication)
        # print(response.status_code)
        # print(response.json())
        
        # print("Sheety json:", response.json())
        # print("To Sheety json:", self.json_to_sheety)
        json_flights_from_sheety = response.json()["flights"]

        for flight in json_flights_from_sheety:
            if flight["destinationCity"] == self.json_to_sheety[0]["destinationCity"]:
                destination_city = flight["destinationCity"]
                try:
                    price = flight["price"]
                except:
                    price = None

                price_is_lower = self.compare_flight_price( 
                                                    city_sheety = destination_city, 
                                                    price_sheety = price)
                if price_is_lower == True:
                    print(f"There is a lower price for the route from {self.json_to_sheety[0]['originCity']} to {destination_city}")
                    json_post_to_sheety = {
                        "flight": self.json_to_sheety[0]
                    }
                    response_post = requests.put(url=f"{self.api_endpoint}/{flight['id']}", 
                                                  json=json_post_to_sheety, 
                                                  auth=self.user_authentication)
                    
                    # print(f"Response for PUT to Sheety: {response_post.status_code}")
                    # print(response_post.text)
                    # 
                    # Notification
                    # Post to spreadsheet
                    print()
                else:
                    print(f"There is no lower price for the route from {self.json_to_sheety[0]['originCity']} to {destination_city}")
                    print()


    def compare_flight_price(self, city_sheety, price_sheety) -> bool:
        """
        Compare flight price from sheety with
        API-Response Price
        """
        if price_sheety is None:
            return True
        elif self.json_to_sheety[0]["price"] <= price_sheety and self.json_to_sheety[0]["destinationCity"] == city_sheety:
            return True
        elif self.json_to_sheety[0]["price"] > price_sheety and self.json_to_sheety[0]["destinationCity"] == city_sheety:
            return False


            
        print("Destination city not found in spreadsheet.")

