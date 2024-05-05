# %%
import requests
import time
import datetime
import ciso8601


current_time = datetime.datetime.now()
current_time_hour = current_time.hour
# current_time_hour  = "19"
current_time_min = current_time.minute

print("Current Time =", current_time)


response = requests.get(url = f"https://api.meteomatics.com/2023-06-02T{current_time_hour}:{current_time_min}:00.000+02:00/t_2m:C/48.8953937,9.1895147/json?model=mix", 
                        auth=('user', 'password'))
response.raise_for_status()

data = response.json()
time_data = ciso8601.parse_datetime(data["data"][0]["coordinates"][0]["dates"][0]["date"])
temp_data = data["data"][0]["coordinates"][0]["dates"][0]["value"]

print(f"Time: {time_data.hour+2}:{time_data.minute}  / Tmeperature: {temp_data} Celsius")

# %%
