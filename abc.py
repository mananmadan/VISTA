#!/usr/bin/python
#import pysftp as sftp
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
import urllib
from bs4 import BeautifulSoup
import wikipedia
#import scrapy
#from scrapy import *
from collections import defaultdict

# graph is a dictionary whith list as its value for implementing the data structure graph
# each graph variable stores revelent categories of thier respective query upto given level



# making connection with given category to its revelant categories

def addEdge(graph,u,v):
    graph[u].append(v)

# inserting edge information in a lift from dictionary

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
# displaying all values for a key in the graph

def show_edges(graph):
    edges=generate_edges(graph)
    for n in edges:
     print (n)

# shortest path between two noedes via dijkstra algorithm

def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


# Creating cookie jar object to extract the image tags

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#login_data = urllib.parse.urlencode({'login' : 'admin', 'pass' : '123'})

opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

#eachthing = wikipedia.page(city_tags[0]['value']).categories
#print(eachthing)

# for scraping informatin from wikipedia

wikipedia.set_lang("en")

def my_f(query):    #extracting wikipedia tags from a query

 #wikiterm = wikipedia.search(query)
 dx = 0
 # To eleminate exceptions in wikipedia categories
 try:
    page = wikipedia.page(query)
 except wikipedia.exceptions.DisambiguationError as e:
  dx=10
 except wikipedia.exceptions.PageError as e:
  #print e
  dx=10
 if dx == 0:
  if urllib.urlopen(wikipedia.page(query).url).getcode() == 200 :
   content = opener.open(wikipedia.page(query).url).read()
   soup2 = BeautifulSoup(content,'html.parser')
   cat1 = soup2.find_all("div",{'class':'mw-normal-catlinks'})
   cat2 = cat1[0].find_all('a')
   d=0
   list=[]
   for i in cat2:
    if d != 0:
     list.append(str(i.text.encode('utf8')))
    d=d+1
 else:
     return 0
 return list

# Adding scraped data to graph
def create_graph(query,lvl,graph):
 lvl = lvl + 1
 templist=[]
 a=0
 if query not in graph :
    templist = my_f(query)
 else:
    for var in graph[query]:
        templist.append(var)
        a=1

 if templist != 0 and len(templist) != 0 :
  if a!=1:
   print(query," ",templist)
   print("\n")
  for i in templist:
   if (a!=1):
    addEdge(graph,query, i)
  for j in templist:
   #print(j)
   if lvl<2:
    if j !=query :
     create_graph(j,lvl,graph)
   else:
    return 0
 else:
    return 0
 if len(templist) == 1 and templist[0]==query :
    return 0

# File Handling

# Adding data to file
def add_to_file(graph,name):
    open("created_graph/"+name+".txt", 'w').close()
    fout = open("created_graph/"+name+".txt","w")
    for node in graph:
        fout.write(node)
        fout.write("\n")
        for neighbour in graph[node]:
            fout.write(neighbour)
            fout.write("\n")
        fout.write("-1\n")
    fout.write("-2\n")

def output_file(query,gname,path):
    fout = open("output5.txt","a")
    fout.write(query)
    fout.write("\n")
    fout.write(gname)
    fout.write("\n")
    #for node in path:
     #   fout.write(node)
      #  fout.write("\n")

    fout.write(str(len(path)))
    fout.write("\n")
    fout.write("-1\n")

# Reading data from file
def read_from_file(graph,name):

    try:
        fin = open("created_graph/"+name+".txt")
    except :
        return 0
    query=fin.readline()
    query=query.replace("\n","")
    while(query and query!="-2"):
        val=fin.readline()
        val=val.replace("\n","")
        while(val and val!="-1"):
            addEdge(graph,query,val)
            val=fin.readline()
            val=val.replace("\n","")
        query=fin.readline()
        query=query.replace("\n","")
    return 1

graph = defaultdict(list)

xl = ["modern encryption techniques","digital","binary digits","modern cryptosystems need","binary strings",
"binary string","based","binary strings","symmetric encryption schemes","block ciphers","plain binary text",
"plaintext bits","ciphertext bits","des","aes","block sizes","stream ciphers","time i.e","technically","stream ciphers",
"block ciphers","block size","block cipher","basic scheme","block cipher","block cipher","plaintext bits","ciphertext bits",
"block size","encryption scheme","key length","block size","avoid","small block size","say","block size","m bits",
"possible plaintext bits combinations","attacker discovers","plain text blocks","ciphertext blocks","dictionary attack",
"plaintext_ciphertext pairs","encryption key","block size","dictionary needs","large block size","large block size",
"such plaintexts","multiples","block size","computer processor","padding","block cipher block","ciphers process blocks",
"block size","bit plaintext","bits needs","redundant information","final block","bits need","redundant bits","complete block",
"too","system insecure","block cipher schemes","vast number","block ciphers schemes","prominent block ciphers","digital encryption",
"des","popular block cipher","_broken_ block cipher","small key size","triple des","variant scheme","des","block ciphers","block ciphers",
"advanced encryption","aes","new block cipher","encryption algorithm","rijndael","aes","design competition","idea","strong block cipher",
"block size","key size","idea","early versions","privacy","pgp","idea","patent issues","feistel block cipher","feistel cipher",
"specific scheme","block cipher","design model","different block ciphers","des","feistel cipher","cryptographic system","feistel",
"cipher structure uses","encryption process","encryption process uses","feistel","multiple rounds","permutation step","feistel structure",
"input block","encryption key","function _f_","r.","output f","xor","mathematical function","l.","real implementation","feistel cipher",
"des","whole encryption key","dependent key","encryption key","round uses","different key","original key","permutation step","round swaps",
"r.","current round","output l","current round","permutation steps form","algorithm design","sub blocks","ciphertext block","difficult part",
"feistel cipher","round function _f_","unbreakable scheme","function needs","important properties","decryption process","feistel",
"ciphertext block","feistel","reverse order","feistel cipher","number","rounds","feistel cipher","inefficient slow encryption",
"decryption processes","number","efficiency security tradeoff","data encryption","des","symmetric key block cipher",
"national institute","standards","nist","des","feistel cipher","feistel","block size","key length","des","effective key length",
"encryption algorithm","check bits","structure","des","des","feistel cipher","des","round function","key","additional processing",
"initial","final permutation","initial","final permutation","final permutations","permutation","cryptography significance","des",
"final permutations","function","des","des","function applies","bit key","bit output","expansion permutation","right input","round key",
"permutation","permutation logic","des","key generation","round key generator creates sixteen","bit keys","bit cipher key","key generation",
"parity","compression p","des","des analysis","des","block cipher","avalanche","plaintext results","completeness","des","weak keys","des",
"block cipher","significant cryptanalytic attacks","des","exhaustive key search","key triple des","3tdes key","des","actual 3tdes key",
"encryption scheme","encryption decryption process","encrypt","plaintext blocks","des","des","des","decryption","reverse process","user",
"triple des","encrypt decrypt encrypt process","des","k2","backwards compatibility","des","triple des","user encrypt plaintext blocks",
"key length","triple des","des","des","advanced encryption","symmetric encryption algorithm","advanced encryption","aes","des","des",
"key size","exhaustive key search attack","triple des","aes","symmetric","key symmetric block cipher","bit data","128/192/256 bit keys",
"stronger","triple des provide","full specification","design details","software","java","aes aes","feistel",
"_substitution permutation network_","specific outputs","interestingly","aes","hence","aes","plaintext block",
"des","aes","aes","bit keys","bit keys","bit keys","rounds uses","bit round key","aes","aes","encryption process",
"typical round","aes","sub processes","round process"
]

for query in xl:
   read_from_file(graph,query)
   create_graph(query,0,graph)    
   add_to_file(graph,query)
   show_edges(graph)
   print("\n")