#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
from datetime import datetime

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_experimental_option("--headless", True)
# Adding Headers
chrome_options.add_argument("--user-agent={HEADERS}")

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.python.org/")


elements_selenium = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# Use selection of unsorted list, then find specific time attribute
date_elements_selenium = [e.find_elements(by=By.CSS_SELECTOR, value="time") for e in elements_selenium][0]

text_elements = [e.text.splitlines()[::-2]  for e in elements_selenium][0]
date_elements = [e.get_attribute("datetime").split("T")[0] for e in date_elements_selenium]
# pprint(text_elements)
# pprint(date_elements)

combined = [{
    "full_name":text_elements[i],
    "time":date_elements[i]
} for i in range(0, len(text_elements))]
pprint(combined)


