#Ed Lee
from random import *
from math import *
from sys import *

if len(argv) > 1:
	n = int(argv[1])
else:
	n = 8
max = n * (n - 1) / 2

def show(board):
	  for r in range(n):
		  s = ""
		  for c in range(n):
			  if (r + c) % 2 == 1:
				  s += chr(27) + "[31;46"
			  else:
				  s += chr(27) + "[31;43"
			  s += "m"
			  if board[c] == r:
				  s += chr(27) + "[30m" + "X"
			  else:
				  s += " "
		  print chr(27) + "[0m" + s + chr(27) + "[0m"
	  print chr(27) + "[0m"

def heuristic(board):
	  h = 0
	  y = 0
	  for x in board:
		  temp = y+1
		  while temp < 8:
			  if(x == board[temp]):
				  h = h+1
			  temp = temp+1
		  xcoord = y+1
		  ycoord = x+1

		  while xcoord < 8 and ycoord < 8:
			  if(ycoord == board[xcoord]):
				  h = h+1
			  xcoord = xcoord+1
			  ycoord = ycoord+1

		  xcoord = y+1
		  ycoord = x-1
		  while xcoord < 8 and ycoord >=0:
			  if(ycoord == board[xcoord]):
				  h = h+1
			  xcoord = xcoord+1
			  ycoord = ycoord-1
		  y = y+1
	  return h

def boards(board): #calculate the correct board
	  finboard = []
	  x = 0
	  for y in board:
		  temp =  y+1
		  while temp < n:
			  tempArr = board[:]
			  tempArr[x] = temp
			  finboard.append(tempArr)
			  temp = temp+1
		  temp2 = y-1

		  while temp2 >=0:
			  tempArr = board[:]
			  tempArr[x] = temp2
			  finboard.append(tempArr)
			  temp2 = temp2 - 1
		  x = x+1
	  return finboard

def hillclimb(): #First Choice
	    attempts = 0
	    ok = 0
	    while attempts < 1000:
		  board = range(n)
		  for x in range(n):
			  board[x] = randint(0, n-1)
		  h = heuristic(board)
		  while h > 0:
			  temp2 = []
			  temp2 = boards(board)
			  shuffle(temp2)
			  oldh=h
			  for xcoord in temp2:
				  if(heuristic(xcoord) < heuristic(board)):
					board = xcoord[:]
					break
			  h = heuristic(board)
			  if oldh==h:
				  break
		  attempts = attempts+1
		  if attempts > 1000:
			  break
		  show(board)
		  if h==0:
			  ok = ok+1
	    print ok

def genetic(): #cut in half, then solve
	  temp = 0
	  genepool = []
	  x = 0
	  parent = (n/3)*4
	  child = (n/3)*2
	  while (x < parent):
		  x = x+1
		  board = range(n)
		  for xcoord in range (n):
			  board[xcoord] = randint(0, n-1)
		  genepool.append(board)
	  while temp==0: #halfening
		  offspring = []
		  size = 0
		  while (size < child):
			  hval = 100
			  for boards in genepool:
				  if (heuristic(boards) < hval):
					  hval = heuristic(boards)
				  if (heuristic(boards) == 0):
					  show(boards)
					  exit(0)
			  for boards in genepool:
				  if (heuristic(boards) == hval):
					  offspring.append(boards)
			  size = size+1
		  y = 0
		  for boards in genepool: #mutation
			  shuffle(offspring)
			  x = 0
			  length = len(boards)
			  while (x < length/2):
				  (genepool[y])[x] = (offspring[1])[x]
				  x = x+1
			  shuffle(offspring)
			  while (x < length):
				  (genepool[y])[x] = (offspring[1])[x]
				  x = x+1
			  if(randint(0,10) > 6):
				  random = randint(0, n-1)
				  genepool[y][random] = randint(0, n-1)
			  y = y+1
                        
hillclimb()
#genetic()
