#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pprint import pprint
TELEPHONE_NUMBER = ""

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--user-agent={HEADERS}")

import time
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.tinder.com/")
login = driver.find_element(by=By.XPATH, value="//*[text()='Anmelden']").click()
time.sleep(3)
login2 = driver.find_element(by=By.XPATH, value="//*[text()='Mit deiner Telefonnummer anmelden']").click()
time.sleep(3)
phone_number = driver.find_element(by=By.CSS_SELECTOR, value="input[name=phone_number]").send_keys(TELEPHONE_NUMBER, Keys.ENTER)
pprint("Enter code in browser")
time.sleep(40)
driver.find_element(by=By.XPATH, value="//*[text()='Zulassen']").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value="//*[text()='Aktivieren']").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value="//*[text()='Akzeptieren']").click()
time.sleep(1)
# driver.find_element(by=By.XPATH, value='//*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button/span/span').click()

for i in range(0,100):
    try:
        time.sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span').click()
        # driver.find_element(by=By.XPATH, value='//*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button/span/span').click()
    except:
        pass

# 