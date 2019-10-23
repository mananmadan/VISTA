#!/usr/bin/python

import pysftp as sftp
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
from bs4 import BeautifulSoup
import wikipedia
import scrapy
from scrapy import *
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#login_data = urllib.parse.urlencode({'login' : 'admin', 'pass' : '123'})

opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

#eachthing = wikipedia.page(city_tags[0]['value']).categories
#print(eachthing)
wikipedia.set_lang("en")
#query = "Rock Concert"
query = "Python"

content = opener.open(wikipedia.page(query).url).read()
#print(content)
soup2 = BeautifulSoup(content,'html.parser')
cat1 = soup2.find_all("div",{'class':'mw-normal-catlinks'})
#cat2 = cat1.find_all('a');

#print(type(cat1))
cat2 = cat1[0].find_all('a')

#print(cat2)

#print(type(cat2))

#print(cat2[1]['title'][0])
temp ='Category:'
count=0
for i in cat2:
 print(type(i['title']))
 temp1 = i['title'].encode('utf-8') 
 for j in temp1:
  count = count+1     
  if(count<=7):
   print('')
  else:
   print(j)
 
  count=0






