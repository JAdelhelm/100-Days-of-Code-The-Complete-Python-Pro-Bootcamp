#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Adding Headers
chrome_options.add_argument("--user-agent={HEADERS}")

driver = webdriver.Chrome(options = chrome_options)


driver.get("https://www.amazon.de/dp/B07T7X4YXS/ref_=list_c_wl_lv_ov_lig_dp_it")
driver.find_element(by=By.ID, value="sp-cc-accept").click()


price_eur = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

price_combined = float(f"{price_eur.text}.{price_cents.text}")
pprint(f"The price is {price_combined} €")




# Closes the active tab
# driver.close()

# Closes the whole browser
# driver.quit()





