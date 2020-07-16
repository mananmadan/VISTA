#!/usr/bin/python2

import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
from bs4 import BeautifulSoup
import wikipedia
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

imagepath = 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg'
googlepath = 'http://images.google.com/searchbyimage?image_url='+imagepath

sourceCode = opener.open(googlepath).read()
soup = BeautifulSoup(sourceCode,'html.parser') 
output = soup.find_all('input', title="Search")
print(output[0]['value'])








