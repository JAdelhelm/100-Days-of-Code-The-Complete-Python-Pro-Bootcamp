#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from pprint import pprint
HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--user-agent={HEADERS}")


driver = webdriver.Chrome(options = chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(4)
driver.find_element(by=By.CLASS_NAME, value="fc-button-label").click()
time.sleep(4)
driver.find_element(by=By.ID, value="langSelect-DE").click()
time.sleep(4)


def check_id():
    find_most_expensive = []
    for i in range(0,10):
        try:
            element = driver.find_element(by=By.ID, value=f"productPrice{i}")
            try: 
                text_of_element = element.text
                element_price = text_of_element.replace(",","")
                element_price = element_price.replace(" million", "e6")
                find_most_expensive.append((i, float(element_price)))
            except: 
                pass
        except:
            pass

    # print(find_most_expensive)
    highest_amount_tuple = sorted(find_most_expensive,reverse=True)
    sorted_index = [i for i,j in highest_amount_tuple]
    # print(highest_amount_tuple)
    # print(sorted_index)
    # Return Index
    return sorted_index

import time
start_time = time.time()

for i in range(0, 100_000):
    current_time = time.time()
    if current_time - start_time >= 8:
        highest_amount_indicies = check_id()
        print(highest_amount_indicies)
        for index in highest_amount_indicies:
            try:
                driver.find_element(by=By.ID, value=f"product{index}").click()
            except Exception as e:
                print(e)
                pass
        start_time = time.time() 
    driver.find_element(By.ID, value="bigCookie").click()
# %%
