#%%
URL = "https://secure-retreat-92358.herokuapp.com/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from pprint import pprint
HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--user-agent={HEADERS}")


driver = webdriver.Chrome(options = chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# driver.find_element(by=By.CSS_SELECTOR, value="input[name=fName]").click()
driver.find_element(by=By.CSS_SELECTOR, value="input[name=fName]").send_keys("")
# driver.find_element(by=By.CSS_SELECTOR, value="input[name=lName]").click()
driver.find_element(by=By.CSS_SELECTOR, value="input[name=lName]").send_keys("")
# driver.find_element(by=By.CSS_SELECTOR, value="input[name=email]").click()
driver.find_element(by=By.CSS_SELECTOR, value="input[name=email]").send_keys("", Keys.ENTER)

# print(element.text)