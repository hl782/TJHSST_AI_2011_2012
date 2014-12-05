#Lab12 - Canny Edge Detection
#Ed Lee
from math import *
def gaussian():
	edgelist = open("vjustice.pgm", 'r').read().split()
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
	print len(glist), len(gxlist), len(gylist)
	return gtotal

def canny():
	gvalues = gaussian()
	edgelist = open("vsmooth.pgm", 'r').read().split()
	outfile = open("vcanny.ppm", 'w')
	outfile.write('P3\n')
	outfile.write('%d %d\n'%(420, 315))
	outfile.write('255\n')
	values = []
	recurhash = {}
	width = edgelist[1]
	height = edgelist[2]
	high_thres = 150
	low_thres = 100
	for x in range(4, len(edgelist)):
		values.append(int(edgelist[x]))
	
	print len(values)
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
	while i < len(values):
		if i in recurhash:
			outfile.write('%d %d %d\n'%(0, 0, 0))
		else:
			outfile.write('%d %d %d\n'%(255, 255, 255))
		i = i+1
	outfile.close()

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

canny()