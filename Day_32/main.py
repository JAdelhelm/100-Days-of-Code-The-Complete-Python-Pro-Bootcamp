import smtplib
from datetime import datetime
from random import choice

if __name__ == "__main__":
    my_email = ""
    password = ""
    with open("quotes.txt") as file:
        quotes = file.readlines()
        file.close()

    quote_of_the_day = choice(quotes)
    # print(quote_of_the_day)
    todays_day = datetime.weekday(datetime.now())
    todays_hour = datetime.now().hour

    if todays_day == 0 and todays_hour == 9:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs="", 
                                msg=f"Subject:Motivation Monday\n\n {quote_of_the_day}")
            connection.close()
    else:
        print("Today is not monday.")
