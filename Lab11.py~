#Lab 11 - Edge Detection
#Ed Lee

def grayscale():
	edgelist = open("vjustice.ppm", 'r').read().split()
	red = []
	blue = []
	green = []
	for x in range (4, len(edgelist), 3):
		red.append(edgelist[x])
	for x in range(5, len(edgelist), 3):
		blue.append(edgelist[x])
	for x in range(6, len(edgelist), 3):
		green.append(edgelist[x])

	length = len(red)	
	outfile=open('vjustice.pgm','w')
	outfile.write('P2\n')
	outfile.write('%d %d\n'%(420,315))
	outfile.write('255\n')
	for x in range(0, length):
		outfile.write('%d\n'%(.30*int(red[x]) + .59*int(blue[x]) + .11*int(green[x])))
	outfile.close()

def smoothing():
	edgelist = open("vjustice.pgm", 'r').read().split()
	width = edgelist[1]
	values = []
	outfile = open('vsmooth.pgm', 'w')
	outfile.write('P2\n')
	outfile.write('%d %d\n'%(420, 315))
	outfile.write('255\n')
	for x in range(4, len(edgelist)):
		values.append(int(edgelist[x]))
	index = 0
	while index < len(values):
		x = index % int(width)
		y = index / int(width)
		if x == 0 or y == 0 or x==int(width)-1 or y==int(edgelist[2])-1: 
			outfile.write('%d\n'%(values[index]))
		else:
			neighborx = []
			neighbory = []
			for i in range(-1, 2):
				for j in range(-1, 2):
					neighborx.append(x+i)
					neighbory.append(y+j)
			retindex = 0
			for x in range(0, 9):
				if x == 0 or x == 2 or x == 6 or x == 8:
					retindex = retindex + values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 1 or x == 3 or x == 5 or x == 7:
					retindex = retindex + 2*values[(neighbory[x]*int(width) + neighborx[x])]
				if x == 4:
					retindex = retindex + 4*values[(neighbory[x]*int(width) + neighborx[x])]
			retindex = retindex/16
			outfile.write('%d\n'%(retindex))
		index = index + 1
	outfile.close()

def gaussian():
	edgelist = open("vjustice.pgm", 'r').read().split()
	width = edgelist[1]
	values = []
	outfile = open('vsmoothgauss.pgm', 'w')
	outfile.write('P2\n')
	outfile.write('%d %d\n'%(420, 315))
	outfile.write('255\n')
	for x in range(4, len(edgelist)):
		values.append(int(edgelist[x]))
	index = 0
	while index < len(values):
		x = index % int(width)
		y = index / int(width)
		if x == 0 or y == 0 or x==int(width)-1 or y==int(edgelist[2])-1:
			outfile.write('%d\n'%(values[index]))
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
			outfile.write('%d\n'%(g))
		index = index + 1
	outfile.close()

def sobel():
	gvalues = gaussian()
	edgelist = open("vjustice.pgm", 'r').read().split()
	outfile = open("vsobel.ppm", 'w')
	outfile.write('P3\n')
	outfile.write('%d %d\n'%(420, 315))
	outfile.write('255\n')
	values = []
	threshold = 100
	for x in range(4, len(edgelist)):
		values.append(int(edgelist[x]))
	index = 0
	while index < len(values):
		if gvalues[index] > threshold:
			outfile.write('%d %d %d\n'%(255, 0, 0))
		else:
			outfile.write('%d %d %d\n'%(255, 255, 255))
		index = index+1
	outfile.close()
	
grayscale()
smoothing()
gaussian()
sobel()