#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
url = 'http://web.mta.info/developers/turnstile.html' 
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
soup.findAll('a')


