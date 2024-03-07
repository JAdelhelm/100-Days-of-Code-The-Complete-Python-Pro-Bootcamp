#%%
from bs4 import BeautifulSoup
import lxml
import requests
from pprint import pprint

url_website = "https://news.ycombinator.com/news"
response = requests.get(url=url_website)
content_soup = response.text
soup = BeautifulSoup(content_soup, "lxml")


article_score =[]
for article_tag, score  in zip(soup.find_all(class_="titleline"), soup.find_all(class_="score")):
    article_score.append((article_tag.get_text(), int(score.get_text().replace("points","").strip())))

sorted_data_article_score = sorted(article_score, key=lambda x: x[1], reverse=True)
pprint(sorted_data_article_score)