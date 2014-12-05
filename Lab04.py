#Lab04: DFS, BFS, Uniform Cost Searches
#Ed Lee 10-03-11
from string import lowercase
from sys import exit
from time import time
from math import sqrt
from heapq import *
import random
begin = raw_input('Starting City: ')
end = raw_input('Ending City: ')
rawlist = open('edge_list_ordered.txt', 'r').read().split('\n')
coordlist = open('xy.txt', 'r').read().split('\n')

ht = {}
xy = {}
for word in rawlist: #Makes list of Neighbors
        word = word.split(',')
        if word[0] in ht:
                ht[word[0]].append(word[-1])
        else:   
                h = []
                h.append(word[-1])
                ht[word[0]] = h

for num in coordlist: #Makes list of Coordinates
        temp = []
        value = num.split(',')
        temp.append(value[1])
        temp.append(value[-1])
        xy[value[0]] = temp

def distance(x1,y1,x2,y2): #Gets distance between 2 cities
        x = (x2-x1)
        y = (y2-y1)
        return sqrt((x*x)+(y*y))
  
def BFS(start, last): #Breath First Search
        myList=[]
        temp = []
        paths = []
        copy = []
        myList.append(start)
        temp.append(0)
        temp.append(start)
        paths.append(temp)
        while len(paths) > 0:
                temp = paths.pop(0)
                if(last == temp[-1]):
                        break
                neighbors = []
                neighbors = ht[temp[-1]]
                for nbr in neighbors:
                        copy = temp[:]
                        if nbr not in myList:
                                myList.append(nbr)
                                copy[0] = copy[0] + distance(int(xy[copy[-1]][0]), int(xy[copy[-1]][-1]), int(xy[nbr][0]),int(xy[nbr][-1]))
                                copy.append(nbr)
                                paths.append(copy)
        return temp

def DFS(start, last): #Depth First Search
        myList=[]
        temp = []
        paths = []
        copy = []
        myList.append(start)
        temp.append(start)
        paths.append(temp)
        while len(paths) > 0:
                if(last == temp[-1]):
                        break
                neighbors = []
                neighbors = ht[temp[-1]]
                for nbr in neighbors:
                        copy = temp[:]
                        if nbr not in myList:
                                myList.append(nbr)
                                ##copy[0] = copy[0] + distance(int(xy[copy[-1]][0]), int(xy[copy[-1]][-1]), int(xy[nbr][0]),int(xy[nbr][-1]))
                                copy.append(nbr)
                                paths.append(copy)
                temp = paths.pop()
        return temp

def UCS(start, last): #Uniform Cost Search - Returns the Cheapest Cost
        myList=[]
        temp = []
        paths = []
        copy = []
        myList.append(start)
        temp.append(0)
        temp.append(start)
        heappush(paths, temp)
        while len(paths) > 0:
                temp = heappop(paths)
                if(last == temp[-1]):
                        break
                neighbors = []
                neighbors = ht[temp[-1]]
                for nbr in neighbors:
                        if nbr in temp:
                                continue
                        copy = temp[:]
                        copy[0] = copy[0] + distance(int(xy[copy[-1]][0]), int(xy[copy[-1]][-1]), int(xy[nbr][0]),int(xy[nbr][-1]))
                        copy.append(nbr)
                        heappush(paths, copy)
        return temp
  
#print BFS(begin, end)
print DFS(begin, end)
#print UCS(begin, end)
