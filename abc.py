#!/usr/bin/python
import pysftp as sftp
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
   if lvl<3:
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

xl = ["spa requirements","gam station process focus","organisation process definition","software management","agnew ane polk engineering",
"peer ken ice","spa requirements","level quantitative process management","software quality management spa requirements level",
"i defect prevention","software company level","india com","dan requirements specification donna king",
"akin times drama queen canon les","vicious non andre ord","functional view","dynamic view mind seiko function dec",
"object state ambition","relations diagram","diagram attributes data dictionary data","data press specification",
"data flow diagram","cam scanner art","employee salary","mary alan data flow diagram process","data flow dalai tow",
"compute terminator","internal agent process stone","employee sale mat agent employee terminator moo holden",
"price report pay slip male objects","data flow diagram level","diagram content diagram waste issue info",
"library infra st supplier schemes","boo les","liable jul ram","ivory book","available limit","search books supplies books",
"payment return book","fine issue book request","basement issue","boone id enrich","emit tool","available ennis den issue",
"book mend","i men id exists i member level","return books approach","data flow diagram","classical linen","cam scanner art",
"ability completeness traceability","consistency details design","una tui quot ness","modify ability semantics",
"tug sri han capability maturity model com","i duty","auth standards organisation blank software companies kernel",
"act city spa key process seas","repeatable com","adam hefner","anime lib spa","requirement management","project planning",
"frost i seasons","software project","i ane sight","subcontract management grad stay module","software quality assurance",
"configuration management","cam scanner art","time data","diagram event part limit","data event","flow que need",
"service bacon scenarios events function mange data","monthly weekly trig que","plain dental management","dental service",
"clos liberia timber thu music","price i","past villas date cd","particular services clinic sends","appointment patient performs",
"complete re local","smiles doctor","content diagram","note fec","apt hunts patient i digital requests","patient services",
"ans formation","record clinic","whoitolaitosent keri corset mil art sustain copy moment","patient record","appointment schedule",
"cam scanner man","time data","date tine","pain ii patient word louis event list","patient record","i click fins","moment request",
"david i services","goal sentiment patient lent uses rat","patio pats ami click bra vail reg appointment","appointments patient",
"palate i patients list","dentists i dentists patient days request","patients patients dentist","patriot guards",
"patient secrets patient records services","cam scanner",
]
for query in xl:
   read_from_file(graph,query)
   create_graph(query,0,graph)    
   add_to_file(graph,query)
   show_edges(graph)
   print("\n")