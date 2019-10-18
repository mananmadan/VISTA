#!/usr/bin/python
import requests

print('Beginning file download with requests')

url = 'https://en.wikipedia.org/wiki/Hybrid_bicycle'
r = requests.get(url)

with open('/home/manan/Downloads/test_wiki.txt', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
