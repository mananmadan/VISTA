from googlesearch import search
import requests
import re

fin = open("output3.txt","r")
words=fin.readlines()
#word1=word1.replace("\n","")
i=0
while(i<len(words)) :
    word1=words[i].replace("\n","")
    i=i+1
    word2=words[i].replace("\n","")
    i=i+3
    regex1='\W'+word1+'\W'
    regex2='\W'+word2+'\W'
    query='"'+word1+'" "'+word2+'"'
    for url in search(query, tld='com', stop=1):
        if(url.find(".pdf",len(url)-5)==-1):
            print(url)
            print(word1+" = ")    
            print(len(re.findall(regex1, requests.get(url).text,  re.IGNORECASE) )  )
            print(word2+" = ")    
            print(len(re.findall(regex2, requests.get(url).text,  re.IGNORECASE) )  )
            print("\n")



