# %%
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "Your Email"
TWITTER_PASSWORD = "Your Password"

from twitterbot import InternetSpeedTwitterBot
if __name__ == "__main__":
    bot = InternetSpeedTwitterBot(down=PROMISED_DOWN, up=PROMISED_UP, user_email=TWITTER_EMAIL, user_password=TWITTER_PASSWORD)
    bot.get_internet_speed()