from tkinter import *
from random import *
from time import sleep
from copy import deepcopy
def setUpCanvas(root):
	root.title("Othello: A Tk/Python Graphics Program")
	canvas = Canvas(root, width=1270, height=780, bg = 'GREY30')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def createMatrix():
	M = [ [0, 0, 0, 0, 0, 0, 0, 0,],
		  [0, 0, 0, 0, 0, 0, 0, 0,],
		  [0, 0, 0, 0, 0, 0, 0, 0,],
		  [0, 0, 0,-1, 1, 0, 0, 0,],
		  [0, 0, 0, 1,-1, 0, 0, 0,],
		  [0, 0, 0, 0, 0, 0, 0, 0,],
		  [0, 0, 0, 0, 0, 0, 0, 0,],
		  [0, 0, 0, 0, 0, 0, 0, 0,],]
	return M

def copyMatrixToScreen():
	ch = chr(9679)
	canvas.create_text(30, 30, text="x", fill='BLACK', font = ('Helvetica',1))	
	
	for r in range(8):
		for c in range(8):
			#canvas.create_rectangle(50+70*r, 70+70*c, 120+70*r, 140+70*c, width = 1, fill='darkgreen')
			if M[r][c] == 1:
				sx = c*70 + 85
				sy = r*70 + 99
				canvas.create_text(sx, sy, text = ch, fill = 'BLACK', font = ('Helvetica', 90, 'bold'))
			if M[r][c] == -1:
				sx = c*70 + 85
				sy = r*70 + 99
				canvas.create_text(sx, sy, text = ch, fill = 'WHITE', font = ('Helvetica', 90, 'bold'))
	
	# highlight available moves
	"""for pt in findAvailableMoves(human):
		canvas.create_rectangle(50+70*pt[0], 70+70*pt[1], 50+70*(pt[0]+1), 70+70*(pt[1]+1), width=1, fill='grey30')"""
	
	canvas.update()

def copyOldBoardToScreen(cc, rr):
	# erase previous board
	canvas.create_rectangle(650, 400, 821, 567, width = 5, fill = 'grey30')
	ch =chr(9679)
	for r in range(8):
		for c in range(8):
			sx = c*20 + 665
			sy = r*20 + 412
			if M[r][c] == 1:
				canvas.create_text(sx, sy, text = ch, fill = 'BLACK', font = ('Helvetica', 20, 'bold'))
			if M[r][c] == -1:
				canvas.create_text(sx, sy, text = ch, fill = 'WHITE', font = ('Helvetica', 20, 'bold'))
		
	canvas.create_text(cc*20 + 665, rr*20 + 413, text = 'B', fill = 'BLACK', font = ('Helvetica', 9, 'bold'))
	canvas.update()
	
def score():
	wt = 0; bt = 0
	for r in range(8):
		for c in range(8):
			if M[r][c] == 1: bt += 1
			if M[r][c] == -1: wt += 1
	return (bt, wt)

def printMatrix(M, msg = "Matrix M:"):
	print("\n", msg)
	print ("     0  1  2  3  4  5  6  7")
	print("   +--------------------------+")
	for r in range(8):
		print (r, "|", end=="")
		for c in range (8):
			if M[r][c] == 1: ch = '#'
			if M[r][c] ==-1: ch = 'O'
			if M[r][c] == 0: ch = '-'
			print ("%3s"%ch, end=="")
		print("  |")
	print ("   +-------------------------+")
	print ("    human    = # = BLACK  =  1")
	print ("    computer = O = WHITE  = -1")

def inRange(r, c):
	return c in range(len(M)) and r in range(len(M))

def toUserCoords(x, y):
	return (x+1, "abcdefgh"[y])

def findAvailableMoves(player):
	moves = []
	for c in range(len(M)):
		for r in range(len(M)):
			if M[r][c] == 0:
				if LocateTurnedPieces(c, r, player) != []: moves.append((c, r))
			'''if M[r][c] == -player:
				#print(toUserCoords(r, c))
				for x in range(c-1, c+2):
					for y in range(r-1, r+2):
						if not inRange(x, y): continue
						if M[x][y] == 0 and LocateTurnedPieces(x, y, player) != []: moves.append((x, y))'''
	return moves

def LocateTurnedPieces(r, c, player):
	if M[r][c] != 0: return []
	totalFlipped = []
	
	# case 1 = R
	flipped = []
	if c < 6 and M[r][c+1] == -player:
		for n in range(1,9):
			if c+n > 7 or M[r][c+n] == 0:
				flipped = []
				break
			if M[r][c+n] == player: break
			flipped.append((r,c+n),)
	totalFlipped += flipped
	
	#case 2 = D
	flipped = []
	if r<6 and M[r+1][c] == -player:
		for n in range(1,9):
			if r+n > 7 or M[r+n][c] == 0:
				flipped = []
				break
			if M[r+n][c] == player: break
			flipped.append((r+n,c))
	totalFlipped += flipped
	
	# case 3 = U
	flipped = []
	if r>1 and M[r-1][c] == -player:
		for n in range(1,9):
			if r-n < 0 or M[r-n][c] == 0:
				flipped = []
				break
			if M[r-n][c] == player: break
			flipped.append((r-n,c))
	totalFlipped += flipped
	
	# case 4 = L
	flipped = []
	if c > 1 and M[r][c-1] == -player:
		for n in range(1,9):
			if c-n < 0 or M[r][c-n] == 0:
				flipped = []
				break
			if M[r][c-n] == player: break
			flipped.append((r,c-n),)
	totalFlipped += flipped
	
	#case 5 = DR
	flipped = []
	if r < 6 and c < 6 and M[r+1][c+1] == -player:
		for n in range(1,9):
			if (r+n) > 7 or (c+n) > 7 or M[r+n][c+n] == 0:
				flipped = []
				break
			if M[r+n][c+n] == player: break
			flipped.append((r+n, c+n))
	totalFlipped += flipped
	
	#case 6 = UL
	flipped = []
	if r >0 and c >0 and M[r-1][c-1] == -player:
		for n in range(1,9):
			if (r-n) < 0 or (c-n) < 0 or M[r-n][c-n] == 0:
				flipped = []
				break
			if M[r-n][c-n] == player: break
			flipped.append((r-n, c-n))
	totalFlipped += flipped
	
	# case 7 = UR
	flipped = []
	if r > 1 and c < 6 and M[r-1][c+1] == -player:
		for n in range(1,9):
			if (r-n) < 0 or (c+n) > 7 or M[r-n][c+n] == 0:
				flipped = []
				break
			if M[r-n][c+n] == player: break
			flipped.append((r-n, c+n))
	totalFlipped += flipped
	
	#case 8 = DL
	flipped = []
	if r <6 and c >0 and M[r+1][c-1] == -player:
		for n in range(1,9):
			if (r+n) > 7 or (c-n) < 0 or M[r+n][c-n] == 0:
				flipped = []
				break
			if M[r+n][c-n] == player: break
			flipped.append((r+n, c-n))
	totalFlipped += flipped
	
	print(totalFlipped)
	
	return totalFlipped

def LocateTurnedPieces4(r, c, player):
	print("Locating turned pieces for ", toUserCoords(r, c), 'for', player);
	# Note: 1. (r, c) MUST be empty.
	#       2. Pieces turned over are of player's color
	#       3. This is the key function for the entire program. It has eight cases.

	# if (r, c) is not empty return
	if M[r][c] != 0: return []
	
	totalFlipped = 0
	pieces = []
	
	# test cases - UL, U, UR, R, DR, D, DL, L
	# way to execute a test case - keep going that way until you find a piece of your own color
	
	# UL
	x = r-1
	y = c-1
	piecesTmp = []
	while True:
		if not inRange(x, y): break
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		x, y = x-1, y-1
	
	# U
	x = r
	y = c-1
	piecesTmp = []
	while True:
		if not inRange(x, y): break
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		y = y-1

	# UR
	x = r+1
	y = c-1
	piecesTmp = []
	while True:
		if not inRange(x, y): break
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		x, y = x+1, y-1
	
	# R
	x = r+1
	y = c
	piecesTmp = []
	while True:
		if not inRange(x, y): break
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		x = x+1
	
	# DR
	x = r+1
	y = c+1
	piecesTmp = []
	while True:
		if not inRange(x, y): break
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		x, y = x+1, y+1

	# D
	x = r
	y = c+1
	piecesTmp = []
	while True:
		if not inRange(x, y): break
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		y = y+1
	
	# DL
	x = r-1
	y = c+1
	piecesTmp = []
	while True:
		if not inRange(x, y): break
		print('Going DL', toUserCoords(x, y))
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		x, y = x-1, y+1
	
	# L
	x = r-1
	y = c
	piecesTmp = []
	while True:
	
		if not inRange(x, y): break
		if M[x][y] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[x][y] == player: pieces += piecesTmp; break
		if M[x][y] == 0: break # should never happen if it's a valid move
		x = x-1
	
	print('Total flipped', totalFlipped, pieces)
	return pieces

def LocateTurnedPieces2(r, c, player):
	if M[r][c] != 0: return []
	totalFlipped = []
	
	# case 1 = R
	flipped = []
	if c < 6 and M[r][c+1] == -player:
		for n in range(1,9):
			if c+n > 7 or M[r][c+n] == 0:
				flipped = []
				break
			if M[r][c+n] == plaer: break
			flipped += ((r,c+n),)
	totalFlipped += flipped
	
	return totalFlipped

def LocateTurnedPieces3(r, c, player, debug = False):
	#print("Locating turned pieces for ", toUserCoords(r, c), 'for', player);
	# Note: 1. (r, c) MUST be empty.
	#       2. Pieces turned over are of player's color
	#       3. This is the key function for the entire program. It has eight cases.

	# if (r, c) is not empty return
	if M[r][c] != 0: return []
	
	totalFlipped = 0
	pieces = []
	
	# test cases - UL, U, UR, R, DR, D, DL, L
	# way to execute a test case - keep going that way until you find a piece of your own color
	
	# UL
	x = r-1
	y = c-1
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going U', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		x, y = x-1, y-1
	
	# U
	x = r
	y = c-1
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going U', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		y = y-1

	# UR
	x = r+1
	y = c-1
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going UR', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		x, y = x+1, y-1
	
	# R
	x = r+1
	y = c
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going R', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		x = x+1
	
	# DR
	x = r+1
	y = c+1
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going DR', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		x, y = x+1, y+1

	# D
	x = r
	y = c+1
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going D', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		y = y+1
	
	# DL
	x = r-1
	y = c+1
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going DL', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		x, y = x-1, y+1
	
	# L
	x = r-1
	y = c
	piecesTmp = []
	while True:
		if not inRange(y, x): break
		if debug == True: print('Going L', toUserCoords(x, y))
		if M[y][x] == -player: totalFlipped += 1; piecesTmp.append((x, y))
		if M[y][x] == player: pieces += piecesTmp; break
		if M[y][x] == 0: print('Exiting because of 0 at',toUserCoords(y, x)); break # should never happen if it's a valid move7
		x = x-1
	
	#print('Total flipped', totalFlipped, pieces)
	return pieces


def copyOldBoard(canvas):
	# draw outer box, with red border
	canvas.create_rectangle(50, 70, 610,630, width = 1, fill    = 'DARKGREEN')
	canvas.create_rectangle(47, 67, 612,632, width = 5, outline = 'RED'  )
	
	# draw 7 horizontal and 7 vertical lines to make the cells
	for n in range(1, 8): # draw horizontal lines
		canvas.create_line(50, 70+70*n, 610, 70+70*n, width = 2, fill = 'BLACK')
	for n in range(1, 8): # draw vertical lines
		canvas.create_line(50+70*n, 70, 50+70*n, 630, width = 2, fill = 'BLACK')
	
	# place score on screen
	canvas.create_rectangle(700, 160, 900, 250, width = 0, fill = 'grey30')
	(BLACK, WHITE) = score()
	stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
	canvas.create_text(800, 200, text = stng, \
					   fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
	stng = "Suggested reply (col, row): (c, 4)"
	canvas.create_text	   (755, 350, text = stng, \
					   fill = 'GREEN',  font = ('Helvetica', 10, 'bold'))
	
	# highlight available moves
	"""for pt in findAvailableMoves(human):
		canvas.create_rectangle(50+70*pt[0], 70+70*pt[1], 50+70*(pt[0]+1), 70+70*(pt[1]+1), width=0, fill='grey30')"""

def setUpInitialBoard(canvas):
	global M; ch = chr(9679)
	
	# print title
	canvas.create_text(330, 50, text = "OTHELLO--a programming assignment", \
					   fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
	
	# print directions
	stng = "DIRECTIONS:\n1) Black moves first. Click on any unoccupied cell.\n\
2. If a player cannot move, play passes to the opponent. \n3) Game ends when \
no legal move is possible.\n4) The player with the most colors on the board \
wins.\n5) A legal move MUST cause some pieces to turn color."
	canvas.create_text(810, 100, text = stng,  \
					   fill = 'WHITE',  font = ('Helvetica', 10, 'bold'))
	
	# draw outer box, with red border
	canvas.create_rectangle(50, 70, 610,630, width = 1, fill    = 'DARKGREEN')
	canvas.create_rectangle(47, 67, 612,632, width = 5, outline = 'RED'  )
	
	# draw 7 horizontal and 7 vertical lines to make the cells
	for n in range(1, 8): # draw horizontal lines
		canvas.create_line(50, 70+70*n, 610, 70+70*n, width = 2, fill = 'BLACK')
	for n in range(1, 8): # draw vertical lines
		canvas.create_line(50+70*n, 70, 50+70*n, 630, width = 2, fill = 'BLACK')
	
	
	# highlight available moves
	'''for pt in findAvailableMoves(human):
		canvas.create_rectangle(50+70*pt[0], 70+70*pt[1], 50+70*(pt[0]+1), 70+70*(pt[1]+1), width=1, fill='grey30')'''
	
	# place letters at bottom
	tab = " " * 8
	stng = 'a' + tab + 'b' + tab + 'c' + tab + 'd' + tab + 'e' + \
				 tab + 'f' + tab + 'g' + tab + 'h'
	canvas.create_text(325, 647, text = stng, \
					   fill = 'DARKBLUE', font = ('Helvetica', 20, 'bold'))
	
	# place digits on left side
	for n in range(1, 9):
		canvas.create_text(30, 35 + n * 70, text = str(n), \
					   fill = 'DARKBLUE',  font = ('Helvetica', 20, 'bold'))

	# copy matrix to screen
	copyMatrixToScreen()
	
	# place score on screen
	## canvas.create_rectangle(800, 200, 960, 350, width = 5, fill = 'grey30')
	(BLACK, WHITE) = score()
	stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
	canvas.create_text(800, 200, text = stng, \
					   fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
	stng = "Suggested reply (col, row): (c, 4)"
	canvas.create_text	   (755, 350, text = stng, \
					   fill = 'GREEN',  font = ('Helvetica', 10, 'bold'))

def illegalClick(x, y, player):
	if x < 52 or x > 609:
		print("Error 1. Mouse is to left or right of board.")
		return True
	
	if y < 62 or y > 632:
		print("Error 2.Mouse is above or below the board.")
		return True
	
	# calculate matrix position
	c = (x-50)//70
	r = (y-70)//70
	if M[r][c] != 0:
		print("ERROR 3: Cell is occupied at r =",r," c =",c)
		return True
	
	flag = 0
	if c < 7 and		   M[r  ][c+1] == -player: return False
	if r < 7 and		   M[r+1][c  ] == -player: return False
	if r > 0 and		   M[r-1][c  ] == -player: return False
	if c > 0 and		   M[r  ][c-1] == -player: return False
	
	if r < 7 and c < 7 and M[r+1][c+1] == -player: return False
	if r > 0 and c > 0 and M[r-1][c-1] == -player: return False
	if r > 0 and c < 7 and M[r-1][c+1] == -player: return False
	if r < 7 and c > 0 and M[r+1][c-1] == -player: return False
	
	print("ERROR 4: no opposite colored neighbors at r =",r," c =",c)
	return True # illegal move

def legalMove(player):
	pieces = []
	for r in range(8):
		for c in range(8):
			pieces += LocateTurnedPieces(r, c, player)
			if pieces != []: break
		if pieces != []: break
	if pieces == []:
		person = 'WHITE'
		if player == 1: person = 'BLACK'
		stng = 'There is no legal move for '+person
		canvas.create_rectangle(655, 260, 957,307, width = 0, fill = 'grey30')
		canvas.create_text     (800, 280, text = stng, fill = 'RED', font = ('Helvetica', 10, 'bold'))
		return False
	return True

def makeComputerReply1():
	from time import sleep
	sleep(1)
	# move into a corner if possible. Make a move that turns over the max number of pieces.
	max = 0
	for r in range(8):
		for c in range(8):
			if M[r][c] == 0:
				pieces = LocateTurnedPieces(r, c, computer)
				L = len(pieces)
				if L > max:
					finalPieces = pieces
					x = c
					y = r
					max = L
	makeMove(x, y, finalPieces, computer)

def makeMove(c, r, pieces, player):
	global M
	# flip pieces to oppposite color of player
	for elt in pieces:
		M[elt[0]][elt[1]] = player
		
		# store legal move in matrix and update screen
		M[r][c] = player
		copyMatrixToScreen()
		
		# erase old score and previous move
		canvas.create_rectangle(650, 160, 960, 310, width = 5, fill = 'grey30')
		
		# print new score
		(BLACK, WHITE) = score()
		stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
		canvas.create_text(800, 200, text = stng, fill = 'WHITE', font = ('Helvetica', 20, 'bold'))
		
		# print previous move
		position = "previous move: "+ str(chr(c + 97))+str(r+1)
		canvas.create_text(800, 250, text = position, fill = 'WHITE', font = ('Helvetica', 20, 'bold'))
		
		if player == computer:
			canvas.create_text(c*20 + 665, r*20 + 412, text = 'W', fill = 'WHITE', font = ('Helvetica', 9, 'bold'))

def quit():
	canvas.create_text(330, 350, text = 'GAME OVER', fill = 'RED', font = ('Helvetica', 40, 'bold'))
	stng = 'THERE ARE NO LEGAL MOVES FOR EITHER PLAYER.'
	canvas.create_rectangle(655,260,957, 307, width = 0, fill = 'grey30')
	canvas.create_text(805, 280, text = stng, fill = 'RED', font = ('Helvetica', 9, 'bold'))

def click(evt):
	# if move is off board, or cell full, or no opp neighbor, then CLICK AGAIN.
	if illegalClick(evt.x, evt.y, human): return
	
	# find matrix coordinates (c,r) in terms of mouse coordinates (evt.x, evt.y)
	c = (evt.x - 50)//70
	r = (evt.y - 70)//70
	
	# if none of the computer's pieces will be turned, then CLICK AGAIN.
	pieces = LocateTurnedPieces(r, c, human)
	if pieces == []: return
	
	# make human move(s) and computer reply/replies.
	copyOldBoardToScreen(c, r)
	makeMove(c, r, pieces, human)
	canvas.create_rectangle(660, 330, 870, 370, width = 0, fill = 'grey30')
	if legalMove(human) and not legalMove(computer): return
	
	#make computer reply/replies (1=black=human, -1=computer=white)
	if legalMove(computer): makeComputerReply1()
	while legalMove(computer) and not legalMove(human):
		makeComputerReply1()

	if not legalMove(human) and not legalMove(computer): quit()
	#note that a legal move for human must now exist.
	return

root=Tk()
canvas   =  setUpCanvas(root)
Me = M   =  createMatrix()
human    =  1 # = Black
computer = -1 # = White

def main():
	global root, canvas
	root.bind('<Button-1>', click)
	setUpInitialBoard(canvas)
	root.mainloop()

if __name__ == '__main__': main()
