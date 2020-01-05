#!/usr/bin/python
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
   if lvl<7:
    if j !=query :
     create_graph(j,lvl,graph)
   else:
    return 0
 else:
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

xl = ["intelligence artificial intelligence goals objective",
            "ai conventional",
            "intelligent computing advantages",
            "disadvantages",
            "ai application",
            "ai",
            "according",
            "henri bergson",
            "artificial objects",
            "different definition",
            "ai","artificial intelligence",
            "artificial intelligence","computer","computer software","hardware","human minds","computer system",
            "intelligent behavior","artificial intelligence","computer science",
            "human intelligence","artificial intelligence","artificial","computer programs","intelligent things",
            "common sense","suppose","chess","b tries","defeat b","such computer","chess computer",
            "expert player","artificial intelligence","converts data","english","french etc","ai","english s w",
            "ai","main goals","ai","computer smarter","human brain","powerful tool","simply","artificial",
            "human beings","human intelligence","model process","useful programs","ai","user","communicate","computers",
            "own language","english","cryptic commands","system languages","application programs","artificial intelligence",
            "useful work","artificial","expert system","decision making","specific domain","less","artificial intelligence"
            ,"powerful computers","cpu","ai","ai","computers","digital equipments corporations","dec","ax","typical system"
            ,"ai s w","ai","high cost","wide range","h w","s w","conventional computers","computer"
            ,"computer programs","conventional languages","c++","cobol","conventional computers","conventional software",
            "intelligent computer","artificial","intelligence software","artificial","intelligence languages","lisp","list",
            "prlog","logic","intelligent computers","language translate","robotic","system air","travel","processing expert",
            "conventional software","artificial","conventional computer","step procedure","mathematical formula","sequential procedure"
            ,"computing","quantitative problems","ai","qualitative problem","conventional software system","doing","laborious jobs",
            "conventional computer system","loop statements","major application area","ai","language","robotics expert","computer vision"]
for query in xl:
    i=7
    j=0
    while i>=j :
     read_from_file(graph,query)
     create_graph(query,i,graph)    
     add_to_file(graph,query)
     show_edges(graph)
     print("\n")
     i=i-1
