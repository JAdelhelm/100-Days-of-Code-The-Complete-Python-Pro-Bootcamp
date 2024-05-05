#%%
# https://pixe.la/
import requests
import numpy as np

USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

### Es wird etwas übergeben, deshalb requests.post() ###
### Erzeugen eines Nutzeraccounts ###
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph1_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "min",
    "type": "float",
    "color": "momiji"
}

headers= {
    "X-USER-TOKEN": TOKEN
}



# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# print(response.url)

### Get Data from Pixela - Get ###
# Only used when data is needed from an API

### Pixel to Pixela - POST ###

from datetime import datetime
import json
date_today = datetime.now()
date_pixel = f"{date_today.year}{date_today.month}{date_today.day-2}"

date_strftime_format = date_today.strftime("%Y%m%d")
print(f"Date with strftime: {date_strftime_format}")

pixel_config = {
    "date": date_pixel,
    "quantity": "20",
    "optionalData": json.dumps({"Amount":"Small Programming session"})
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph1_config['id']}"

response = requests.post(url=graph_endpoint, json=pixel_config, headers=headers)
print(response.text)




### Update Pixels - PUT ###

# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

# pixel_update_config = {
#     "quantity": "20",
#     "optionalData": json.dumps({"Amount":"Small Programming session"})
# }

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph1_config['id']}/{date_strftime_format}"

# response = requests.put(url=update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)




### Delete Pixels - DELETE ###

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph1_config['id']}/{date_pixel}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)