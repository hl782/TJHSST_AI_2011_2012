from random import choice
black, white, empty, outer = 1, 2, 0, 3
directions = [-11, -10, -9, -1, 1, 9, 10, 11]

def bracket(board, player, square):
	opp = opponent_color(player)
	for d in directions:
		k = square + d
		if board[k] is not opp:
			continue
		while board[k] is opp:
			k = k + d
		if board[k] is player:
			k = k - d
			while k != square:
				board[k] = player
				k = k - d

def would_bracket(board, player, square):
	opp = opponent_color(player)
	for d in directions:
		k = square + d
		if board[k] is not opp:
			continue
		while board[k] is opp:
			k = k + d
		if board[k] is player:
			return True
	return False

def get_legal_moves(board, player):
	possible = []
	for row in range(10, 90, 10):
		for col in range(1, 9):
			square = row + col
			if board[square] is not empty:
				continue
			if would_bracket(board, player, square):
				possible.append(square)
	return possible

def opponent_color(player):
	if player is black: 
		return white
	return black

def h(board):
	hblack, hwhite = 0,0
	for elem in board:
		if elem == black:
			hblack = hblack+1
		if elem == white:
			hwhite = hwhite+1
	if player is white:
		return hwhite-hblack
	return hwhite+hblack

def pick(board,player):
	poss = get_legal_moves(board,player)
	if len(poss) == 0:
		return None:
	choices = get_legal_moves(board,player)
	length = len(choices)
	limit = [choices[0],choices[-1]]
	return choice(limit)    
