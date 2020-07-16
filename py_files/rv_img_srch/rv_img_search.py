#!/usr/bin/python

import pystp as sftp
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

#def imageLookup():
    #s = sftp.Connection(host = "http://pythonprogramming.net",
                       #username = "python",
                        #password = "rules")
    #localpath = ''
    #numToAdd = str(int(time.time()))
    #remotepath = '/var/www/imagerec/currentImage'+numToAdd+'.jpg'
    #s.put(localpath,remotepath)
    #s.close()
    #imagepath = 'http://pythonprogramming.net/imagerec/currentImage'+numToAdd+'.jpg'
imagepath = 'https://github.com/shikhar-scs/Keldec_dataset/blob/master/dataset_2/image2.jpg?raw=true'
googlepath = 'http://images.google.com/searchbyimage?image_url='+imagepath

sourceCode = opener.open(googlepath).read()
soup = BeautifulSoup(sourceCode,'html.parser')       
 
city_tags = soup.find_all('input', title="Search")
print(city_tags[0]['value'])

#eachthing = wikipedia.page(city_tags[0]['value']).categories
#print(eachthing)
wikipedia.set_lang("en")
#query = (city_tags[0]['value'])
query = "Vehicle"
WikiPage = wikipedia.page(title = query,auto_suggest = True)
var1="Articles"
var2="articles"
var3="Wikipedia"
var4="wikipedia"
cat = WikiPage.categories
for i in cat:
    result=i.find(var1)
    result+=i.find(var2)
    result+=i.find(var3)
    result+=i.find(var4)
    if result  == -4: 
        print (i)
        print("*******************************************************\n")
        #query=i
        #WikiPage = wikipedia.page(title = query,auto_suggest = True)
        #cat1 = WikiPage.categories
        #for j in cat1:
        #result1=j.find(var1)
        #result1+=j.find(var2)
        #result1+=j.find(var3)
        #result1+=j.find(var4)
        #if result1  == -4: 
        #print (j)
        #print("--------------------------------------------------------\n")
      







