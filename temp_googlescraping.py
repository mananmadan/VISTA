from googlesearch import search
import requests
import re
a=[]
data=[]
def sort_urls(data):
    newdata=[]
    for word,text in zip(a,data):
        text=text.split()      
        i=0
        
        while(i<len(text)-4):
            j=0
            while(j<len(text)-4):
                if(  int(text[j+1])<=int(text[j+4])  ):
                    if( int(text[j+2]) <=int(text[j+5]) ):
                        temp1=text[j]
                        temp2=text[j+1]
                        temp3=text[j+2]
                        text[j]=text[j+3]
                        text[j+1]=text[j+4]
                        text[j+2]=text[j+5]
                        text[j+3]=temp1
                        text[j+4]=temp2
                        text[j+5]=temp3
                    elif(  min(int(text[j+1]),int(text[j+2])) < min(int(text[j+4]),int(text[j+5]))  ):
                        temp1=text[j]
                        temp2=text[j+1]
                        temp3=text[j+2]
                        text[j]=text[j+3]
                        text[j+1]=text[j+4]
                        text[j+2]=text[j+5]
                        text[j+3]=temp1
                        text[j+4]=temp2
                        text[j+5]=temp3
                elif(min(int(text[j+1]),int(text[j+2])) < min(int(text[j+4]),int(text[j+5]))):
                    temp1=text[j]
                    temp2=text[j+1]
                    temp3=text[j+2]
                    text[j]=text[j+3]
                    text[j+1]=text[j+4]
                    text[j+2]=text[j+5]
                    text[j+3]=temp1
                    text[j+4]=temp2
                    text[j+5]=temp3
                        
                elif( abs(int(text[j+1])-int(text[j+2]) ) == abs(int(text[j+4])-int(text[j+5])   ) and ( (text[j+1]=='0' or text[j+2]=='0') or int(text[j+1]+text[j+2])  < int(text[j+4]+text[j+5]))):
                    temp1=text[j]
                    temp2=text[j+1]
                    temp3=text[j+2]
                    text[j]=text[j+3]
                    text[j+1]=text[j+4]
                    text[j+2]=text[j+5]
                    text[j+3]=temp1
                    text[j+4]=temp2
                    text[j+5]=temp3
                j=j+3
            i=i+3
        strtemp=word+"\n"
        i=0
        while(i<len(text)-3):
            strtemp+=text[i]+"\n"+text[i+1]+" "+text[i+2]+"\n"
            i=i+3
        strtemp=strtemp+"-1\n"
        newdata.append(strtemp)
    for x in newdata:
        print (x)
    return newdata
   
    

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
            data.append(strtemp)
            strtemp=""
            var=query
    fin.close()
    open("urlw8.txt","w").close()
    
    return 1

read_from_file()
data=sort_urls(data)
fout= open("urlw8.txt","w")
for x,y in zip(a,data):
    fout.write(x+"\n")
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













