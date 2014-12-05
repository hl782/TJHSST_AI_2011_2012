#Ed Lee
#Lab 16 - Coloring Problem
from math import *
from random import *
mastercolors = ['r', 'b', 'g', 'y']
def colorcheck(n, colors):
	for states in n:
		compare = colors[states]
		for neigh in n[states]:
			if compare == colors[neigh]:
				return True
	return False

def recur(n, c, p):
	if len(c) >= len(n):
		if colorcheck(n, c) == 0:
			print c
			exit(0)
	else:
		for k in n:
			if k not in c:
				temp = k
		for colors in p[temp]:
			c[temp] = colors
			for nbr in n[temp]:
				if colors in p[nbr]:
					p[nbr].remove(colors)
			recur(n, c,p)
			del c[temp]
			#print c
			#
			# add back in colors to p[nbr] if removed by temp
			#

def mapcolor():
	#mlist = open('austrailia.txt', 'r').read().split()
	mlist = open('states_48.txt', 'r').read().split()
	n = {}
	ncolor = {}
	posCol = {}
	x = 0
	while x < len(mlist):
		if mlist[x] in n.keys():
			n[mlist[x]].append(mlist[x+1])
		else:
			temp = []
			temp.append(mlist[x+1])
			n[mlist[x]] = temp
		if mlist[x+1] in n.keys():
			n[mlist[x+1]].append(mlist[x])
		else:
			temp = []
			temp.append(mlist[x])
			n[mlist[x+1]]=temp
		x = x+2
	print n
	for elem in n:
		temp = mastercolors
		posCol[elem] = temp[:]
	ncolor = recur(n, ncolor, posCol)
	
mapcolor()