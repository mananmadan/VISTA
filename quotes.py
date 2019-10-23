#!/usr/bin/python
import wikipedia
import requests
import pprint
import urllib3
from urllib3 import PoolManager
import time
from bs4 import BeautifulSoup
import requests
import urllib
#
#imagepath = 'https://github.com/shikhar-scs/Keldec_dataset/blob/master/dataset_2/image2.jpg?raw=true'
#googlepath = 'http://images.google.com/searchbyimage?image_url='+imagepath
#sourceCode =requests.get(googlepath,allow_redirects=False)
#print(sourceCode.content)
#urls = []
#soup = BeautifulSoup(sourceCode.content,'html.parser') 
#for page in soup.find_all('a'):
#  #print(page)
#  urls.append(page.attrs['href'])
#print(urls[0])
#mp=urllib.request.urlopen(urls[0])
#data=mp.read()
#print(data)

#soupmp=BeautifulSoup(mp.content,'html.parser')
#city_tags = soupmp.find_all('input', title="Search")
#print(city_tags[0]['value'])
#
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
#print("\n")
#print(list[0])
    
