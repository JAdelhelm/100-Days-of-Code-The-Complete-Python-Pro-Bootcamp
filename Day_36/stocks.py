# %%
import requests
from datetime import datetime
import textwrap
import inspect
import alpha_vantage


class StockChangeRecognizer():
    def __init__(self, parameters: {}, stock_name: str, news_parameters=None) -> None:
        self.parameters = parameters
        self.news_parameters = news_parameters
        self.stock_name = stock_name

        self.price_ratio_percentage = None
        self.status_code = None

        self.json_data = None
        self.json_time_series = None
        self.open_price_today = None
        self.open_price_yesterday = None
        # Nur an den Wochentagen geöffnet
        self.yesterday_date = None
        self.before_yesterday_date = None

        self._stock_message = "\n"
        self._big_delta = False


    def get_data(self):
        API_URL = "https://www.alphavantage.co/query"
        response = requests.get(API_URL, params=self.parameters)
        self.status_code = response.status_code

        print(f"Status code: {self.status_code}")
        print(f"API-Request: {response.url}")
        print()

        if self.status_code == 200:
            self.json_data = response.json()
            try:
                self.json_time_series = self.json_data["Time Series (Daily)"]
                list_of_keys = list(self.json_time_series.keys())
                # Letzter Öffnungstag
                self.yesterday_date = list_of_keys[0]
                # Vorletzer Öffnungstag
                self.before_yesterday_date = list_of_keys[1]

                # print(self.yesterday_date, self.before_yesterday_date)

                print(self.json_time_series)
            except Exception as e:
                self.status_code = 429
                print("❗❗❗"+ response.text, "\n")
        else:
            print(f"Error: Received status code {self.status_code}")

    def get_open_stock_price_yesterday(self):
        if self.status_code == 200:
            yesterday_json = self.json_time_series[self.yesterday_date]
            open_price_yesterday = float(yesterday_json["2. high"])

            return open_price_yesterday

    def get_open_stock_price_before_yesterday(self):
        if self.status_code == 200:
            before_yesterday_json = self.json_time_series[self.before_yesterday_date]
            open_price_before_yesterday = float(
                before_yesterday_json["2. high"])

            return open_price_before_yesterday

    def check_if_increased_or_decreased(self):
        self.get_data()
        open_price_before_yesterday = self.get_open_stock_price_before_yesterday()
        open_price_yesterday = self.get_open_stock_price_yesterday()

        try:
            base_price_ratio = open_price_before_yesterday / 100

            self.price_ratio_percentage = (
                    open_price_yesterday / base_price_ratio) - 100
            
            if self.status_code == 200:
                if self.price_ratio_percentage <= -5.0:
                    self._stock_message += f"\n\n🔴 {self.stock_name}: Price decreased by  ↘️ - {round(self.price_ratio_percentage,2)}%"
                    self._big_delta = True
                elif self.price_ratio_percentage >= 5.0:
                    self._stock_message += f"\n\n🟢 {self.stock_name}: Price increased by  ↗️ + {round(self.price_ratio_percentage,2)}%"
                    self._big_delta = True
                else:
                    if round(self.price_ratio_percentage, 2) >= 0:
                        self._stock_message += f"\n\n ⚪ {self.stock_name}: Price has only minor changes ↗️ + {round(self.price_ratio_percentage,2)}%"
                    else:
                        self._stock_message += f"\n\n⚪ {self.stock_name}: Price has only minor changes ↘️ - {round(self.price_ratio_percentage,2)}%"
        except Exception as e:
            raise e



    def get_news(self, limit=3):
        self.news_parameters["from"] = self.before_yesterday_date
        self.news_parameters["to"] = self.yesterday_date

        if self.news_parameters is None:
            raise ValueError("No News-parameters have been defined.")

        response = requests.get(
            "https://newsapi.org/v2/everything", params=self.news_parameters)
        reponse_json_news = response.json()
        # print(response.url)

        self._stock_message += f"\n🟨🟨🟨 {self.stock_name} 🟨🟨🟨\n"
        for news_ in range(limit):
            try:
                actual_news_title = reponse_json_news["articles"][news_]["title"]
                actual_news_content = reponse_json_news["articles"][news_]["content"]
                try:
                    cleaned_news_title = actual_news_title.replace(
                        "\r", "").replace("\n", " ")
                    cleaned_news_content = actual_news_content.replace(
                        "\r", "").replace("\n", " ")
                except:
                    pass
                self._stock_message += "⏹️ Headline: " + cleaned_news_title + "⏹️\n"
                self._stock_message += "- " + cleaned_news_content + "\n\n"
            except:
                print(f"Reached limit of news at {news_}\n")
                break

        self._stock_message = inspect.cleandoc(self._stock_message)
        self._stock_message = textwrap.dedent(self._stock_message)

        return self._stock_message

    def print_message(self):
        print()
        print(self._stock_message)

    @property
    def stock_message(self):
        return self._stock_message

    @property
    def big_delta(self):
        return self._big_delta

    def send_news_to_mail(self):
        if self.price_ratio_percentage <= -5 or self.price_ratio_percentage >= 5 and self._stock_message is not None:
            # Send mail with message self._stock_message
            pass


# %%
