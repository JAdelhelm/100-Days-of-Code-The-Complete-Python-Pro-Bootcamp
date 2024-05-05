#%%
import requests
import lxml
from bs4 import BeautifulSoup
import random
from pprint import pprint
import time

PRODUCT_URL = "https://www.amazon.de/dp/B07T7X4YXS/ref_=list_c_wl_lv_ov_lig_dp_it"

HEADERS={"accept-language": "en-US,en;q=0.9",
         "accept-encoding": "gzip, deflate, br",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}


response = requests.get(PRODUCT_URL, headers=HEADERS)
print(response.url,"\n")

soup = BeautifulSoup(response.text, "lxml")


check_whole_price = soup.find(class_="a-price-whole")
check_price_fraction= soup.find(class_="a-price-fraction")

float_price = float(f"{check_whole_price.getText().replace(',','')}.{check_price_fraction.getText()}")

pprint(soup.find(class_="a-price-a-offscreen"))
o={}

try:
    o["title"]=soup.find('h1',{'id':'title'}).text.strip()
except:
    o["title"]=None

pprint(o["title"][:])
pprint(f"Price of Board: {float_price}€")


### Implement E-Mail Notification ###
