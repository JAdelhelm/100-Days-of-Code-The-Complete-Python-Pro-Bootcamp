from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}



class InternetSpeedTwitterBot():
    def __init__(self, down, up, user_email, user_password) -> None:
        self.down = down
        self.up = up

        self.user_email = user_email
        self.user_password = user_password

        self.down_actual = None
        self.up_actual = None

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--user-agent={HEADERS}")
        self.driver = webdriver.Chrome(options = chrome_options)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="onetrust-accept-btn-handler").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//*[text()='Go']").click()
        time.sleep(60)
        try:
            wait = WebDriverWait(self.driver, 10)  # Wait for up to 10 seconds
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')))
            close_button.click()
        except:
            pass
        time.sleep(3)


        self.down_actual = float(self.driver.find_element(by=By.CLASS_NAME, value='download-speed').text)
        self.up_actual = float(self.driver.find_element(by=By.CLASS_NAME, value='upload-speed').text)

        pprint(f"Down: {self.down_actual}")
        pprint(f"Up: {self.up_actual}")

    def tweet_at_provider(self):
        # Not implemented
        pass
