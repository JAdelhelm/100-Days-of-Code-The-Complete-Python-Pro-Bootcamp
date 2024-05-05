#%%
from bs4 import BeautifulSoup
import lxml

contents = open("website.html").read()
soup = BeautifulSoup(contents, 'lxml')
print(soup.prettify())

for tag in soup.find_all(name="a"):
    print(tag.get("href"))
# %%
