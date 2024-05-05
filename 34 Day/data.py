import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}


def question_data():
    response = requests.get("https://www.otriviata.com/api.php", params=parameters)
    response_to_json = response.json()

    return response_to_json["results"]
