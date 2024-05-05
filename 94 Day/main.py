"""
Automate the Google Dinosaur Game.

# https://trex-runner.com/
"""
#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui
import time

driver = webdriver.Chrome()
driver.get("https://elgoog.im/t-rex/")
delay = 15 # seconds


try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))
    myElem.click()
    print( "Page is ready!")
except Exception:
    print( "Loading took too much time!")

action = ActionChains(driver)
action.key_down(Keys.SPACE).send_keys().perform() 

# Site is ready - Here it should use pyautogui
time.sleep(3)

dino = pyautogui.locateCenterOnScreen('dino.png', confidence=0.9)
x = int(dino[0])
y = int(dino[1])

offset = 100

while True:
    try:
        # location = pyautogui.locateOnScreen('cactus.png', confidence=0.7)
        if pyautogui.pixelMatchesColor(x + int(offset), y, (90, 90, 90), tolerance=150):
                pyautogui.press('space')
                offset += 0.7

    except pyautogui.ImageNotFoundException:
        # print('ImageNotFoundException: image not found')
        pass







# driver.close()