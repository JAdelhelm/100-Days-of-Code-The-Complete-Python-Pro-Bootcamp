import numpy as np

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, json_data_flights) -> None:
        self.json_data_flights = json_data_flights

        self._flight_data = []

    @property
    def flight_data(self):   
        return self._flight_data


    def format_flight_data(self, return_x_cheapest_flights):
        check_min_price = []

        if return_x_cheapest_flights == 1:
            len_of_id_flights = len(self.json_data_flights)
        else: 
            len_of_id_flights = len(self.json_data_flights)-1

        for recent_id in range(len_of_id_flights):
            temp_id = self.json_data_flights[recent_id]

            price = temp_id["price"]
            origin_city = temp_id["cityFrom"]
            origin_airport = temp_id["flyFrom"]
            destination_city = temp_id["cityTo"]
            destination_airport = temp_id["flyTo"]
            local_departure = temp_id["local_departure"].split("T")[0]
            local_arrival = temp_id["local_arrival"].split("T")[0]
            nights_in_dest = temp_id["nightsInDest"]
            airlines = temp_id["airlines"][0]

            data_flights_formatted = {
                "originCity":origin_city,
                "originAirport":origin_airport,
                "destinationCity": destination_city,
                "destinationAirport": destination_airport,
                "departureDate": local_departure,
                "arrivalDate": local_arrival,
                "price":price,
                "nightsInDestination": nights_in_dest,
                "airline":  airlines
                # "adults": 2
            }

            self._flight_data.append(data_flights_formatted)

            check_min_price.append(price)
            # print(flight_data)
            # print(f"{flight_data.destination_city}: £{flight_data.price}")
            # print(temp_id_dict)
        self._flight_data = self._flight_data[:return_x_cheapest_flights]
        print(f"The lowest price is at {np.min(check_min_price)} €")
        
        return self._flight_data