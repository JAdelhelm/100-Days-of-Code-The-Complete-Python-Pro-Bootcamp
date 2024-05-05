import requests
from requests.auth import HTTPBasicAuth

class UserClub:
    def __init__(self, user_name, user_password, api_endpoint) -> None:
        self.user_name = user_name
        self.user_password = user_password
        self.api_endpoint = api_endpoint

        self.auth_user = HTTPBasicAuth(username=self.user_name, password=self.user_password)

        print("Welcome to JAdel's Flight Club.")
        print("We find the best flight deals and email you.")

        self.first_name = str(input("What is your first name?"))
        self.last_name = str(input("What is your last name?"))
        self.email = str(input("What is your email?"))
        self.email_confirmation = str(input("Type your emial again."))

        if self.email.lower() != self.email_confirmation.lower(): print("Your confirmation of email is wrong!")
        else: 
            self.add_user_to_spreadsheet()
            print("You're in the club!")
        

    def add_user_to_spreadsheet(self):
        json_user_add = {"user" : {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email":self.email
        }}
        response = requests.post(url=self.api_endpoint,json=json_user_add, auth=self.auth_user)
        print("Successfully added!")
        print(response.status_code)
        print(response.text)