#!/usr/bin/python

import pysftp as sftp
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#login_data = urllib.parse.urlencode({'login' : 'admin', 'pass' : '123'})

opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

def imageLookup():
    #s = sftp.Connection(host = "http://pythonprogramming.net",
    #                   username = "python",
    #                    password = "rules")
    #localpath = '/pic.png'
    #numToAdd = str(int(time.time()))
    #remotepath = '/var/www/imagerec/currentImage'+numToAdd+'.png'
    #s.put(localpath,remotepath)
    #s.close()
    #pythonprogramming.net/imagerec/currentImage

    imagepath = 'http://i.gyazo.com/82ed00642007a857db454cfd19034cae.png'
    googlepath = 'http://images.google.com/searchbyimage?image_url='+imagepath

    sourceCode = opener.open(googlepath).read()

    



imageLookup()



