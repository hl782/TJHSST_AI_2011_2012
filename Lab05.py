#A-Star Search
#Ed Lee

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
  
  
def AStar(start, last): #A* Search - Optimized UCS with heuristic
	myList=[]
	temp = []
	paths = []
	copy = []
	heuristic = distance(int(xy[start][0]),int(xy[start][-1]),int(xy[last][0]),int(xy[last][-1]))
	myList.append(start)
	temp.append(heuristic)
	temp.append(0)
	temp.append(start)
	heappush(paths, temp)
	while len(paths) > 0:
		temp = heappop(paths)
		if(last == temp[-1]):
			break
		neighbors = ht[temp[-1]]
		for nbr in neighbors:
			if nbr in temp: continue
			copy = temp[:]
			#copy[1] = copy[1] + distance(int(xy[copy[-1]][0]), int(xy[copy[-1]][-1]), int(xy[nbr][0]),int(xy[nbr][-1]))
			#heuristic = distance(int(xy[nbr][0]),int(xy[nbr][-1]),int(xy[last][0]),int(xy[last][-1]))
			#copy[0]=copy[1]+heuristic
			copy.append(nbr)
			heappush(paths, copy)
	return temp
  
  
print AStar(begin, end)
