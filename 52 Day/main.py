#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import time 

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
SIMILIAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--user-agent={HEADERS}")

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.instagram.com/")
time.sleep(2)
driver.find_element(by=By.XPATH, value="//*[text()='Alle Cookies erlauben']").click()
time.sleep(4)
driver.find_element(by=By.CSS_SELECTOR, value="input[name=username]").send_keys(USERNAME)
driver.find_element(by=By.CSS_SELECTOR, value="input[name=password]").send_keys(PASSWORD, Keys.ENTER)
time.sleep(10)
try: driver.find_element(by=By.XPATH, value="//*[text()='Alle Cookies erlauben']").click()
except Exception as e: print(e)
time.sleep(5)
try: driver.find_element(by=By.XPATH, value="//*[text()='Jetzt nicht']").click()
except Exception as e: print(e)
time.sleep(5)
try: driver.find_element(by=By.XPATH, value="//*[text()='Jetzt nicht']").click()
except Exception as e: print(e)
time.sleep(2)
try: driver.find_element(by=By.CSS_SELECTOR, value="svg[aria-label=Suche]").click()
except Exception as e: print(e)
time.sleep(2)
try: driver.find_element(by=By.CSS_SELECTOR, value="input[aria-label=Sucheingabe]").send_keys(SIMILIAR_ACCOUNT)
except Exception as e: print(e)
time.sleep(2)
try: driver.find_element(by=By.CSS_SELECTOR, value="a[href^='/chefsteps/']").click()
except Exception as e: print(e)
time.sleep(2)
try: driver.find_element(by=By.CSS_SELECTOR, value="a[href^='/chefsteps/follower']").click()
except Exception as e: print(e)
time.sleep(2)


from selenium.common import NoSuchElementException, ElementClickInterceptedException
def follow(driver):
    #Chefsteps followers.
    people = driver.find_elements(By.XPATH,
                                        "//button[@class=' _acan _acap _acas _aj1- _ap30']")

    #To follow each follower in the pop-up.
    for persons in people:
        try:
            persons.click()
        except ElementClickInterceptedException:
            try:
                driver.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']").click()
                continue
            except Exception:
                print("Sorry, something went wrong")
                pass
        time.sleep(1)
    print("Bot Successful 🙂")


import names
for i in range(10):
    time.sleep(2)
    try: 
        driver.find_element(by=By.CSS_SELECTOR, value="input[aria-label=Sucheingabe]").send_keys(names.get_first_name().lower()[:2])
        time.sleep(4)
    except Exception as e: print(e)
    try: 
        follow(driver)
    except Exception as e: print(e)
    try: driver.find_element(by=By.CSS_SELECTOR, value="input[aria-label=Sucheingabe]").clear()
    except Exception as e: print(e)


