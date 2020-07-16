#!/usr/bin/python
import wikipedia
import requests
import pprint

from urllib3 import PoolManager
import time
from bs4 import BeautifulSoup
import requests
import urllib

wikipedia.set_lang("en")
query = "python"
response = requests.get(wikipedia.page(query).url)
soup2 = BeautifulSoup(response.content,'html.parser')
cat1 = soup2.find_all("div",{'class':'mw-normal-catlinks'})
cat1 = soup2.find_all("div",{'class':'mw-normal-catlinks'})
cat2 = cat1[0].find_all('a')
d=0
list=[]
for i in cat2:
  if d != 0:
    list.append(i.text)
  d=d+1
print(list)
    
