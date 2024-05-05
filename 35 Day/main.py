# %%
import requests
import os
import numpy as np
import textwrap
import inspect
from twilio.rest import Client
import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
import time


class UmbrellaChecker():

    def __init__(self, latitude, longitude, API_KEY, forecasts) -> None:
        self.weather_ids = []
        self.temperature = []

        self.longitude = longitude
        self.latitude = latitude
        self.API_KEY = API_KEY
        self.forecast = forecasts

        self.save_message = ""

        self.parameters = {}
        self.set_parameters()

    def set_parameters(self):
        self.parameters = {
            "lat": self.latitude,
            "lon": self.longitude,
            "appid": self.API_KEY,
            # The next 4 timestamp - forecasts, e.g. 3*4 = 12 hours
            "cnt": 4,
        }

    def get_ids(self):
        """
        Use the API from OpenWeatherMap to get forecasts of the temperature and the weather conditions.
        """
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast", params=self.parameters)
        response.raise_for_status()
        response_json = response.json()

        list_of_ids = response_json["list"]

        weather_ids_temp = []
        temperature_main_temp = []
        for forecast_i in range(len(list_of_ids)):

            id_per_forecast = list_of_ids[forecast_i]["weather"][0]["id"]
            # print(list_of_ids[forecast_i])
            weather_ids_temp.append(id_per_forecast)

            temperature_per_forecast = list_of_ids[forecast_i]["main"]["temp"]
            # print(temperature_per_forecast)
            temperature_main_temp.append(temperature_per_forecast)

        temperature_per_forecast = self.kelvin_to_celsius(
            temperature_main_temp)
        self.temperature = temperature_per_forecast
        # print(temperature_per_forecast)

        self.weather_ids = weather_ids_temp

        return weather_ids_temp

    def check_for_umbrella(self):
        """
        Checks if an umbrella is needed in the next X hours (here 12).
        """
        if len(self.weather_ids) == 0:
            print("Getting weather ids...")
            self.get_ids()
            # print(self.weather_ids)

        for id in self.weather_ids:
            if id < 700:
                self.save_message = f"""
                                    Bring an umbrella ☔, it will be raining today.
                                    
                                    The temperature in the next 12 hours will be around {round(np.median(self.temperature),2)}°C
                                    """
                break

    def kelvin_to_celsius(self, temp_k: list):
        """
        Converts a list of temperatures with Kelvin to Celsisus.
        """
        temp_converted = []
        for t in temp_k:
            calc_t = t - 273.15
            temp_converted.append(calc_t)

        return temp_converted

    def send_sms_alert(self,  account_sid: str, auth_token: str, phone_number_from: str, phone_number_to: str):
        """
        Send SMS via Twilio: https://www.twilio.com/de-de
        """
        self.save_message = inspect.cleandoc(self.save_message)
        self.save_message = textwrap.dedent(self.save_message)

        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=self.save_message,
                            from_=phone_number_from,
                            to=phone_number_to
                        )

    def send_mail_alert(self, your_email: str, to_addrs_mail: str, your_password: str):
        """
        Send Mails via PythonAnywhere: https://www.pythonanywhere.com/
        """

        if len(self.save_message) == 0:
            self.check_for_umbrella()

        self.save_message = inspect.cleandoc(self.save_message)
        self.save_message = textwrap.dedent(self.save_message)

        ### Send E-Mail to yourself ###
        msg = EmailMessage()
        msg.set_content(self.save_message)

        msg["Subject"] = "Weather alert!"
        # msg["From"] = your_email
        msg["To"] = to_addrs_mail

        server = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
        server.login(user=your_email, password=your_password)
        server.send_message(msg)
        server.quit()

        ### Send E-Mail to second person ###
        # msg = EmailMessage()
        # msg.set_content(self.save_message)

        # msg["Subject"] = "Weather alert!"
        # # msg["From"] = your_email
        # msg["To"] = enter_email_for_second_person

        # server = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
        # server.login(user=your_email, password=your_password)
        # server.send_message(msg)
        # server.quit()


if __name__ == "__main__":

    u_checker = UmbrellaChecker(latitude=enter_your_latitude, longitude=enter_your_longitude,
                                API_KEY=enter_your_api_key_from_open_weather, forecasts="4")
    u_checker.check_for_umbrella()
    u_checker.send_mail_alert(your_email=enter_your_mail, your_password=enter_your_password,
                              to_addrs_mail=enter_your_adress_mail)
