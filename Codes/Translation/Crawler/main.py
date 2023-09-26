import json
import os

import bs4
import requests
from bs4 import BeautifulSoup
import lxml
import re

DIR_NAME = 'words'
os.makedirs(DIR_NAME, exist_ok=True)
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

BASE_URL = 'https://www.mortezajavid.com/articles/names-of-diseases-in-english/'

url = f"{BASE_URL}"
f = requests.get(url, headers=headers)
soup = BeautifulSoup(f.content, 'lxml')
table = soup.findAll('table')[0]
lines = table.findAll('tr')
data = []
for line in lines:
    contents = line.findAll('td')
    persian = contents[0].getText()
    english = contents[1].getText()
    data.append({"en": english, "fa": persian})

print(len(data))

with open(f"{DIR_NAME}/data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
