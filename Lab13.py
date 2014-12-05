#Ed Lee - Hough Transform
#Pd 1
from math import *
from random import *
import sys
import os

def gaussian():
	edgelist = open("shapes.pgm", 'r').read().split()
	width = edgelist[1]
	values = []
	glist = []
	gxlist=[]
	gylist=[]
	gtotal = []
	high = 150
	low = 50
	for x in range(4, len(edgelist)):
		values.append(int(edgelist[x]))
	index = 0
	while index < len(values):
		x = index % int(width)
		y = index / int(width)
		if x == 0 or y == 0 or x==int(width)-1 or y==int(edgelist[2])-1:
			glist.append(values[index])
			gxlist.append(0)
			gylist.append(0)
		else:
			neighborx = []
			neighbory = []
			for i in range(-1, 2):
				for j in range(-1, 2):
					neighborx.append(x+i)
					neighbory.append(y+j)
			gx = 0
			gy = 0
			for x in range(0, 9):
				if x == 3 or x == 4 or x == 5:
					gx = gx + 0
				if x == 0 or x == 2:
					gx = gx + -1*values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 1:
					gx = gx + -2*values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 6 or x == 8:
					gx = gx + 1*values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 7:
					gx = gx + 2*values[(neighbory[x]*int(width) + neighborx[x])]
			for x in range(0, 9):
				if x == 1 or x == 4 or x == 7:
					gy = gy + 0
				if x == 0 or x == 6:
					gy = gy + 1*values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 3:
					gy = gy + 2*values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 2 or x == 8:
					gy = gy + -1*values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 5:
					gy = gy + -2*values[(neighbory[x]*int(width) + neighborx[x])]
			g = abs(gx) + abs(gy)
			gxlist.append((gx))
			gylist.append((gy))
			glist.append(g)
		index = index+1
	gtotal.append(glist)
	gtotal.append(gxlist)
	gtotal.append(gylist)
	return gtotal

def canny(filename):
	gvalues = gaussian()
	edgelist = open("shapes.pgm", 'r').read().split()
	outfile = open("shapescanny.ppm", 'w')
	outfile.write('P3\n')
	outfile.write('%d %d\n'%(420, 315))
	outfile.write('255\n')
	values = []
	recurhash = {}
	width = edgelist[1]
	height = edgelist[2]
	high_thres = 150
	low_thres = 100
	cannytable = []
	for x in range(4, len(edgelist)):
		values.append(int(edgelist[x]))
	index = 0
	while index < len(values):
		x = index % int(width)
		y = index / int(width)
		if gvalues[0][index] > high_thres:
			angle = degrees(atan2(gvalues[2][index], gvalues[1][index]))
			angle = (int(angle)/45)*45
			if angle <= 0:
				angle = angle + 360
			direction = angle + 90
			recur(gvalues, recurhash, direction, x, y, width, height)
		index = index + 1		
	i = 0
	return recurhash

def recur(g,rhash, theta, x, y, w, h):
	if g[0][(y*int(w))+x] <= 100 or x == 0 or y == 0 or x == int(w)-1 or y == int(h)-1: #if gvalue of is lower than threshold break or border pixel
		return
	else:
		if theta == 0:
			newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y-1*int(w))+x]>  g[0][(y*int(w))+x] or g[0][(y+1*int(w))+x]>  g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x+1, y, w, h)
			else:
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x+1, y, w, h)
		elif theta == 45:
			newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y-1*int(w))+x-1]> g[0][(y*int(w))+x] or g[0][(y+1*int(w))+x+1]> g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x+1, y-1, w, h)
			else:
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x+1, y-1, w, h)
		elif theta == 90:
		  	newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y*int(w))+x+1] >  g[0][(y*int(w))+x] or g[0][(y*int(w))+x-1]> g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x, y-1, w, h)
			else:
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x, y-1, w, h)
		elif theta == 135:
			newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y+1*int(w))+x-1] >  g[0][(y*int(w))+x] or g[0][(y-1*int(w))+x+1] >  g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x-1, y-1, w, h)
			else:
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x-1, y-1, w, h)
		elif theta == 180:
		  	newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y-1*int(w))+x] >  g[0][(y*int(w))+x] or g[0][(y+1*int(w))+x] >  g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x-1, y, w, h)
			else:
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x+1, y, w, h)
		elif theta == 225:
			newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y-1*int(w))+x-1] >  g[0][(y*int(w))+x] or g[0][(y+1*int(w))+x+1] >  g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x-1, y+1, w, h)
			else:
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x-1, y+1, w, h)
		elif theta == 270:
			newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y*int(w))+x-1] >  g[0][(y*int(w))+x] or g[0][(y*int(w))+x+1] >  g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x, y+1, w, h)
			else:				
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x, y+1, w, h)
		elif theta == 315:
			newtheta = degrees(atan2(g[2][(y*int(w))+x], g[1][(y*int(w))+x]))
			newtheta = (int(theta)/45)*45
			if newtheta <= 0:
				newtheta = theta + 360
			newdir = newtheta + 90
			if g[0][(y+1*int(w))+x-1] >  g[0][(y*int(w))+x] or g[0][(y-1*int(w))+x+1]> g[0][(y*int(w))+x]:
				recur(g, rhash, newdir, x+1, y+1, w, h)
			else:
				rhash[(y*int(w))+x] = None
				recur(g, rhash, newdir, x+1, y+1, w, h)

def recurvote(votemap,  angle, row, col):
	if(int(row) == 0 or int(col) == 0 or int(row) == len(votemap)-1 or int(col) == len(votemap[0])-1):
		return
	votemap[int(row)][int(col)] +=1
	index = int(angle)/45
	x = [0, -1, -1, -1, 0, 1, 1, 1]
	y = [1, 1, 0, -1, -1, -1, 0, 1] 
	recurvote(votemap, angle,row+x[index],col+y[index])

def votes(filename, edgemap, cannytable):
	pi = 4*atan(1)
	votearray = []
	for elem in cannytable:
		templist = []
		for line in array:
			templist.append(line)
		votearray.append(templist)
	r = 0
	while r < len(votearray):
		c = 0
		while c < len(votearray[r]):
			votearray[r][c] = 0
			c+=1
		r+=1
	for key in edgemap:
	  a = key
	  if edgemap[key] == True:
		split = a.split(' ')
		n = int(split[0])
		col = int(split[1])
		angle = atan2(cannytable[n][col][1], cannytable[n][col][0]) * 180/pi
		if angle < 0:
			angle += 360
		recurvote(votearray, angle,n, col)
		secondangle = 0
		if(angle>=180):
			secondangle = angle-180
		else:
			secondangle = angle+180
		recurvote(votearray, secondangle, n, col)
	size = int(raw_input("Enter size"))   #bins
	bins = {}
	    rowcounter = 0
	      while rowcounter < len(votearray)/size:
		      colcounter = 0
		      while colcounter < len(votearray[0])/size:
			      a = str(rowcounter) + ' ' + str(colcounter)
			      bins[a] = 0
			      colcounter+=1
			      rowcounter+=1
	row = 0
	      while row < len(votearray):
		      col = 0
		      while col < len(votearray[0]):
				newrow = row/size
				newcol = col/size
				key = str(newrow) + ' ' + str(newcol)
				bins[key]+=votearray[row][col]
				col+=1
				row+=1
	r = 0    
	while r < len(votearray):
		c=0
		while c< len(votearray[r]):
			newr = r/size
			newc = c/size
			key = str(newr) + ' '+ str(newc)
			filename.write(str((255-(bins[key])/(size/2))))
			filename.write('\n')
			c+=1
		r+=1

def hough():
	cannytable = canny()
	filearray = open("shapes.ppm".read().split('\n')[:-1]
	edgemap = {}
	splitarray = filearray[1].split(' ')
	row = 0
	counter = 3
	while row < int(splitarray[1]):
		col = 0
		while col <  int(splitarray[0]):
			a = str(row) + ' ' + str(col)
				if(filearray[counter] != '255 255 255'):
					edgemap[a] = True
				else:
					edgemap[a] = False
				col+=1
			counter+=1
		row+=1
	votesfile = open("shapesbins.pgm", 'w') 
	votesfile.write('P2\n')
	votesfile.write(filearray[1])
	votesfile.write('\n')
	votesfile.write('255\n')
	cast_votes(votesfile, edgemap, cannytable)
