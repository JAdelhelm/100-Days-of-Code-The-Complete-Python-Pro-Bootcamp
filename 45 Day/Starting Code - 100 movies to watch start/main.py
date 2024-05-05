#%%
import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint
import re

URL = ""

# Write your code below this line 👇
response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, "lxml")

all_titles = soup.find_all(class_=["h3" ,"title"])
# all_titles = soup.find_all(name="h3", class_=["title"])
# pprint(soup.find("title").string)

title_list = []
for title in all_titles:
    try:
        title_list.append(re.findall(r"(^\d+\).*)", title.string)[0])
    except:
        pass

# pprint(sorted(title_list, reverse=True))

title_list_sorted = title_list[::-1]


with open("./topMovies.txt","w+") as f:
    for movie in title_list_sorted:
        f.write(movie+"\n")

