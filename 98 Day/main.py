"""
Automate points collection with Microsoft edge.
https://rewards.bing.com/?ref=status
"""

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import time 

import pyautogui

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}



edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--user-agent={HEADERS}")
# edge_options.add_argument("--headless")

driver = webdriver.Edge(options = edge_options)
driver.get("https://rewards.bing.com/?ref=status")

try:
    sync_button = pyautogui.locateOnScreen('./sync.png', confidence=0.8, minSearchTime=5)
    pyautogui.click(sync_button)
except Exception as e:
    print(e)

elements = driver.find_elements(By.XPATH, "//mee-card")
# print(elements)

try:
    for element in elements:
        element.click()
except: 
    pass

driver.close()