#!/usr/bin/python

import pysftp as sftp
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
from bs4 import BeautifulSoup
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
   


#imageLookup()






