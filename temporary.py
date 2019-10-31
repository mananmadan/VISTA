#!/usr/bin/python

import pysftp as sftp
import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
import urllib
from bs4 import BeautifulSoup
import wikipedia
import scrapy
from scrapy import *

class Graph:


    


    graph_dict={}


    


    def addEdge(self,node,neighbour):  


        if node not in self.graph_dict:


            self.graph_dict[node]=[neighbour]


        else:


            self.graph_dict[node].append(neighbour)


            


    def show_edges(self):


        for node in self.graph_dict:


            for neighbour in self.graph_dict[node]:


                print("(",node,", ",neighbour,")")
  
    def find_shortest_path(self, start, end, path=[]):
        #print(type(path))        
        #print(type(start))
        path.append(start)
        #print(type(path))
        if start == end:
            return path
        if not start in self.graph_dict:
            return None
        shortest = None
        for node in self.graph_dict[start]:
            #print(type(path))
            #print(type(node))
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                print(newpath)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


g= Graph()
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#login_data = urllib.parse.urlencode({'login' : 'admin', 'pass' : '123'})

opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

#eachthing = wikipedia.page(city_tags[0]['value']).categories
#print(eachthing)
wikipedia.set_lang("en")


def my_f(query):
 
 if urllib.urlopen(wikipedia.page(query).url).getcode() == 200 : 
  content = opener.open(wikipedia.page(query).url).read()
  soup2 = BeautifulSoup(content,'html.parser')
  cat1 = soup2.find_all("div",{'class':'mw-normal-catlinks'})
  cat2 = cat1[0].find_all('a')
  d=0
  list=[]
  for i in cat2:
   if d != 0:
    list.append(str(i.text))
   d=d+1
   
  return list

query = "Food"

def create_graph(query,lvl,g):
 lvl = lvl + 1
 templist = my_f(query)
 print(query," ",templist)
 print("\n")
 for i in templist:
  g.addEdge(query, i)
 for j in templist:
  #print(j)
  if lvl<4 :
   if j !=query :
    create_graph(j,lvl,g)
  else :
   return 0
   

create_graph(query,0,g)
g.show_edges()
path2=[]
p1=g.find_shortest_path('Cooking','Domestic life')
print(p1)
print(len(p1))
 

   
 
   
 
 





