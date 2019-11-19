from googlesearch import search
import requests
import re

word123="OveN"
regex='\W'+word123+'\W'
for url in search('"Oven" "Waterfall Model"', tld='com', stop=1):
    print(url)
    
    print(len(re.findall(regex, requests.get(url).text,  re.IGNORECASE) )  )


