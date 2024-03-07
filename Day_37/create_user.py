#%%
# https://pixe.la/
import requests
import numpy as np

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "",
    "notMinor": "yes"
}

### Es wird etwas übergeben, deshalb requests.post() ###
### Erzeugen eines Nutzeraccounts ###

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)