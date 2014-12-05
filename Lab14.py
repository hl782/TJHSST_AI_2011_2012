#Lab 14 - Schelling's Agent Problem
#Ed Lee - Pd. 1
from random import *
def schelling():
	evenrow = ['o','x','o','x','o','x','o','x']
	oddrow = ['x','o','x','o','x','o','x','o']
	matrix = []
	for x in range(0,8):
		  if x%2 == 0:
			  matrix.append(evenrow[:])
		  else:
			  matrix.append(oddrow[:])
	matrix[0][0] = '_'
	matrix[0][7] = '_'
	matrix[7][0] = '_'
	matrix[7][7] = '_'
	count = 0
	while count < 20:
		randx = randint(0, 7)
		randy = randint(0, 7)
		if matrix[randx][randy] != '_':
			matrix[randx][randy] = '_'
			count = count+1
		else:
			randx = randint(0,7)
			randy = randint(0,7)
	count = 0
	while count < 5:                
		randx = randint(0,7)
		randy = randint(0,7)
		xoro = randint(0, 1)
		if matrix[randx][randy] == '_':
			if xoro == 0:
				matrix[randx][randy] = 'x'
			else:
				matrix[randx][randy] = 'o'
			count = count+1
		else:
			randx = randint(0,7)
			randy = randint(0,7)
	satcount = 0
	for x in range(0, 8):
		for y in range(0,8):
			if matrix[x][y] != '_':
				n = getneighbor(matrix, x, y)
				if satisfied(matrix, x, y, n) == False:
					satcount = satcount+1
	print 'Unsatisfied Count: ', satcount
	rounds = 0
	while satcount != 0:
		satcount = 0
		for x in range(0,8):
			for y in range(0,8):
				if matrix[x][y] != '_':
					haha = 0
					if matrix[x][y] == 'x':
						haha = 0
					if matrix[x][y] == 'o':
						haha = 1
					n = getneighbor(matrix, x, y)
					if satisfied(matrix,x,y,n) == False:
						satcount = satcount+1
						everywhere = geteverywhere(matrix)
						random = randint(0, len(everywhere[0])-1)
						if haha == 0:
							matrix[everywhere[0][random]][everywhere[1][random]] = 'x'
						if haha == 1:
							matrix[everywhere[0][random]][everywhere[1][random]] = 'o'
						matrix[x][y] = '_'
		rounds = rounds+1
		print 'Unsatisfied Count: ', satcount
	print rounds

def getneighbor(board, x, y):
	total = 0
	xcount = 0
	ocount = 0
	l = []
	if x-1 > -1 and y-1 > -1:
		if board[x-1][y-1] == 'x':
			total = total+1
			xcount = xcount+1
		if board[x-1][y-1] == 'o':
			total = total+1
			ocount = ocount+1
	if x-1 > -1:
		if board[x-1][y] == 'x':
			total = total+1
			xcount = xcount+1
		if board[x-1][y] == 'o':
			total = total+1
			ocount = ocount+1
	if x-1 > -1 and y+1 < 8:
		if board[x-1][y+1] == 'x':
			total = total+1
			xcount = xcount+1
		if board[x-1][y+1] == 'o':
			total = total=1
			ocount = ocount+1
	if y-1 > -1:
		if board[x][y-1] == 'x':
			total = total+1
			xcount = xcount+1
		if board[x][y-1] == 'o':
			total = total+1
			ocount = ocount+1
	if y+1 < 8:
		if board[x][y+1] == 'x':
			total = total+1
			xcount = xcount+1
		if board[x][y+1] == 'o':
			total = total+1
			ocount = ocount+1
	if x+1 < 8 and y-1 > -1:
		if board[x+1][y-1] == 'x':
			total = total+1
			xcount = xcount+1
		if board[x+1][y-1] == 'o':
			total = total+1
			ocount = ocount+1
	if x+1 < 8:
		if board[x+1][y] == 'x':
			total = total+1
			xcount = xcount+1
		if board[x+1][y] == 'o':
			total = total+1
			ocount = ocount+1
	if x+1 < 8 and y+1 < 8:
		if board[x+1][y+1] == 'x':
			total = total+1
			xcount = xcount +1
		if board[x+1][y+1] == 'o':
			total = total+1
			ocount = ocount +1
	l.append(total)
	l.append(xcount)
	l.append(ocount)
	return l

def satisfied(board, x, y, nlist):
	  if nlist[0] == 1 or nlist[0] == 2:
		  if board[x][y] == 'x':
			  if nlist[1] >= 1:
				  return True
			  else:
				  return False
		  if board[x][y] == 'o':
			  if nlist[2] >= 1:
				  return True
			  else:
				  return False
	  if nlist[0] == 3 or nlist[0] == 4 or nlist[0] == 5:
		  if board[x][y] == 'x':
			  if nlist[1] >= 2:
				  return True
			  else:
				  return False
		  if board[x][y] == 'o':
			  if nlist[2] >= 2:
				  return True
			  else:
				  return False
	  if nlist[0] == 6 or nlist[0] == 7 or nlist[0] == 8:
		  if board[x][y] == 'x':                        
			  if nlist[1] >= 3:
				  return True
			  else:
				  return False
		  if board[x][y] == 'o':
			  if nlist[2] >= 3:
				  return True
			  else:
				  return False

def geteverywhere(board):
	everywhere = []
	everyx = []
	everyy = []
	for u in range(0, 8):
		for v in range(0,8):
			if board[u][v] == '_':
				everyx.append(u)
				everyy.append(v)
	everywhere.append(everyx)
	everywhere.append(everyy)
	return everywhere

def printboard(board):
        for x in range(0, len(board)):
                print board[x]
                print '\n'

schelling()

