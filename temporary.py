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

def my_f(query):
 content = opener.open(wikipedia.page(query).url).read()
 soup2 = BeautifulSoup(content,'html.parser')
 cat1 = soup2.find_all("div",{'class':'mw-normal-catlinks'})
 cat2 = cat1[0].find_all('a')
 d=0
 list=[]
 for i in cat2:
  if d != 0:
   list.append(str(i.text))
  d=d+1
 print(query,":",list,"\n")
 return list

query = "Rock Concert"

templist = my_f(query)
 

 

   
 
   
 
 





