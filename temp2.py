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


graph = defaultdict(list)
graph2=defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
def show_edges(graph):
    edges=generate_edges(graph)
    for n in edges:
     print (n)
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




cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#login_data = urllib.parse.urlencode({'login' : 'admin', 'pass' : '123'})

opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

#eachthing = wikipedia.page(city_tags[0]['value']).categories
#print(eachthing)
wikipedia.set_lang("en")
def my_f(query):
 #wikiterm = wikipedia.search(query)
 dx = 0
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

query = "traffic signals"

def create_graph(query,lvl,graph):
 lvl = lvl + 1
 templist = my_f(query)
 if templist != 0 and len(templist) != 0 :
  print(query," ",templist)
  print("\n")
  for i in templist:
   addEdge(graph,query, i)
  for j in templist:
   #print(j)
   if lvl<5 :
    if j !=query :
     create_graph(j,lvl,graph)
   else:
    return 0
 else:
    return 0
query2="Machine Learning"
create_graph(query,0,graph)
show_edges(graph)
create_graph(query2,2,graph2)
show_edges(graph2)
for n in graph[query] :
    p=find_shortest_path(graph2,query2,n)
    if p != None :
        print p
for n in graph2[query2] :
    p=find_shortest_path(graph,"traffic signals",n)
    if p != None :
        print p






