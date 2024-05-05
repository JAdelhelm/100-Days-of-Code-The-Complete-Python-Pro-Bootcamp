"""
Build a custom web scraper to collect data on things that you are interested in.
"""
#%% 
from bs4 import BeautifulSoup
import requests
import os
import pytesseract
from PIL import Image
import shutil

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

get_html_txt = requests.get("https://evosportsfuel.de/").text


soup_evo = BeautifulSoup(get_html_txt, "html.parser")
# print(soup_evo.prettify())
# print(soup_evo.get_text())

links_with_potential_code = []
# Extract rabatt code
for link in soup_evo.find_all('img'):
    if "week" in link.get('src'):
        links_with_potential_code.append(link.get('src'))
        print(link.get('src'))


try: os.mkdir("./img")
except: pass

extracted_text = []

for image_link in links_with_potential_code:
    img_clean_link = f"https:{image_link}"

    response = requests.get(img_clean_link, stream = True)
    with open('./img/img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    image = Image.open("./img/img.png")
    text = pytesseract.image_to_string(image)
    extracted_text.append(text)

with open("extracted.txt", "w") as f:
    for line in extracted_text:
        f.write(f"{line}")

