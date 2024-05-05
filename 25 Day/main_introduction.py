import pandas as pd
import csv

# data = open("weather_data.csv","r").readlines()
# print(data)

# with open("weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)



# data = pd.read_csv("weather_data.csv")
# print(data["temp"].max())

# monday = data[data.day == "Monday"]
# monday.temp = monday.temp * 1.8 + 32
# print(monday)


# Create DataFrame from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76, 56, 65]
# }

# data_new = pd.DataFrame(data_dict)
# print(data_new)

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(df.columns)
# print(df.groupby(df["Primary Fur Color"]).count())
# df.groupby()

df_squir_col = pd.DataFrame(df["Primary Fur Color"].groupby(df["Primary Fur Color"]).count().sort_values(ascending=False))
print(df_squir_col)