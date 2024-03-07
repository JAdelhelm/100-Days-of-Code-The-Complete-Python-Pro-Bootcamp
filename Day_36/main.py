#%%

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

from stocks import StockChangeRecognizer
from sendmail import SendEmail

if __name__ == "__main__":
    COMPANIES = ["DB", "EBAY", "PLTR", "SPCE"]
    COMPANIE_NAMES = ["Deutsche Bank", "eBay", "Palantir", "Virgin Galactic"]

    PARAMETERS = {
        "function": "TIME_SERIES_DAILY",
        "outputsize": "compact",
        "datatype": "json",
        "apikey": ""
    }

    PARAMETERS_NEWS = {
        "apiKey": "",
        # "q":"+Deutsche Bank",
        "searchIn" : "title,content",
        "language": "de",
        "sortBy": "popularity"

    }

    stock_messages_dict = {}
    for company, company_name in zip(COMPANIES, COMPANIE_NAMES):
        # print(company, company_name)
        PARAMETERS["symbol"] = company

        PARAMETERS_NEWS["q"] = f"+{company_name}"
        # print(PARAMETERS)

        StockObject = StockChangeRecognizer(parameters=PARAMETERS, news_parameters=PARAMETERS_NEWS, stock_name=company_name)
        # StockObject.check_if_increased_or_decreased()
        StockObject.get_news(limit=3)
        # StockObject.print_message()

        # Message wird nur hinzugefügt wenn außergewöhnliches Delta
        if StockObject.big_delta == True:
            stock_messages_dict[company] = StockObject.stock_message
    
    SendEmailObject = SendEmail(dict_of_companies_messages=stock_messages_dict)
    # print(SendEmailObject.mail_message)
    SendEmailObject.send_mails(your_email="", your_password="",
                              to_addrs_mail="")

