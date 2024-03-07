#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pprint import pprint
USER_NAME = ""
PASSWORD = ""

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--user-agent={HEADERS}")


driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.linkedin.com/")
import time
driver.find_element(by=By.XPATH, value="/html/body/nav/div/a[2]").click()
time.sleep(1)
driver.find_element(by=By.ID, value="username").send_keys(USER_NAME)
driver.find_element(by=By.ID, value="password").send_keys(PASSWORD, Keys.ENTER)
time.sleep(3)

driver.get("https://www.linkedin.com/jobs/")
driver.find_element(by=By.ID, value="jobs-search-box-keyword-id-ember25").send_keys("Data Analyst", Keys.ENTER)

# Actual Application is not implemented, just login 