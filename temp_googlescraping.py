from googlesearch import search
import requests
import re
a=[]
data=[]
def read_from_file():

    try:
        fin = open("urlw8.txt")
    except :
        return 0
    query=fin.readline()
    strtemp=""
    query=query.replace("\n","")
    var=query
    while(query):
        while(query and query!="-1"):
            query=fin.readline()
            strtemp+=query
            query=query.replace("\n","")
        query=fin.readline()
        query=query.replace("\n","")
        if(query):
            a.append(var)
            data.append(var+"\n")
            data.append(strtemp)
            strtemp=""
            var=query
    fin.close()
    open("urlw8.txt","w").close()
    
    return 1

read_from_file()
fout= open("urlw8.txt","w")
for y in data:
    fout.write(y)

fin = open("output3.txt","r")
words=fin.readlines()
#word1=word1.replace("\n","")
i=0
while(i<len(words)) :
    word1=words[i].replace("\n","")
    i=i+1
    word2=words[i].replace("\n","")
    i=i+3
    if word2 not in a:
        regex1='\W'+word1+'\W'
        regex2='\W'+word2+'\W'
        query='"'+word1+'" "'+word2+'"'
        fout.write(word2+"\n")
        for url in search(query, tld='com', stop=10):
            if(url.find(".pdf",len(url)-5)==-1):
                test=1
                try:
                    page=requests.get(url).text
                except :
                    test=0
                if test!=0 :
                    fout.write(url)
                    fout.write("\n")    
                    fout.write(str(len(re.findall(regex1, page ,  re.IGNORECASE) ) )  )
                    fout.write(" ")    
                    fout.write(str(len(re.findall(regex2, page ,  re.IGNORECASE) ) )  )
                    fout.write("\n")
        fout.write("-1\n")


