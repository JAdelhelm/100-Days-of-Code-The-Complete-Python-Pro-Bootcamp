# %%


APP_ID = ""
API_KEY = ""


headers_nutri = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    # "query" : "gym for 1 hour",
    "gender": "male",
    "weight_kg": "90",
    "height_cm": "183",
    "age": "28"
}


def pass_workout_to_nutritionix(parameters, headers_nutri):
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    response = requests.post(url=exercise_endpoint,
                             json=parameters, headers=headers_nutri)
    # print(response.status_code)
    print(response.json())

    return response.json()


def retrieve_from_nutritionix(json_to_sheety, user_authentication):
    today_date = datetime.now()
    exercise_date = today_date.strftime("%d/%m/%Y")
    exercise_time = today_date.strftime("%H:%M:%S")
    
    f"{today_date.hour}:{today_date.minute}"
    exercise_name = json_to_sheety["exercises"][0]["user_input"]
    exercise_duration_min = json_to_sheety["exercises"][0]["duration_min"]
    exercise_calories = json_to_sheety["exercises"][0]['nf_calories']

    json_parameters_workout = {
        "workout": {
            "datum": exercise_date,
            "uhrzeit": exercise_time,
            "exercise": exercise_name.title(),
            "dauer": exercise_duration_min,
            "kalorien": exercise_calories
            }
    }

    response = requests.post(
        url="https://api.sheety.co/5d3280a58c1483d800de9673872f2086/training/workouts",
        json=json_parameters_workout, auth=user_authentication)
    print(response.status_code)
    print(response.json())
    print(response.text)


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import json
    from datetime import datetime
    input_user_name = str(input("Input your username: "))
    input_password = str(input("Input your password: "))

    user_authentication = HTTPBasicAuth(input_user_name, input_password)

    input_query = str(input("Tell me which workout you did"))
    parameters["query"] = input_query

    json_training = pass_workout_to_nutritionix(
        parameters=parameters, headers_nutri=headers_nutri)

    retrieve_from_nutritionix(json_to_sheety=json_training, user_authentication=user_authentication)
    print(json_training)
