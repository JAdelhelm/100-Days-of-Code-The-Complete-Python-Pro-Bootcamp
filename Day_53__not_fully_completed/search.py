#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import time 

class SearchApp():
    def __init__(self, driver) -> None:
        self.driver = driver

    def accept_cookies_etc(self):
        self.driver