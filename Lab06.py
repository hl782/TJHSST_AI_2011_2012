#Ed Lee
#Lab 06 - Sliding Tile Puzzle
from Tkinter import *
from sys import exit
from random import shuffle
from math import sqrt
from math import fabs
grid=[]
rectangle = []
display = []
w,h=1000, 1000
x,y,dx,dy=75, 30, 120, 120
root=Tk()
canvas=Canvas(root,width=w,height=h,bg='white')

def click(evnt):
	global x,y, grid
	x,y=evnt.x,evnt.y
	count = 0
	index = 0
	while count < len(grid):
		if grid[count] == '':
			index = count
			break
		count = count + 1
	xClick = evnt.x
	yClick = evnt.y
	xindex = xClick/150
	yindex = yClick/100	
	adjIndex = 0
	adjIndex = (yindex * 4) + xindex
	if (adjIndex == (index+1) or adjIndex == (index-1) or adjIndex == (index+4) or adjIndex == (index-4)) and (adjIndex < (index +5) or adjIndex > (index - 5) or adjIndex > (index -1) or adjIndex < (index-1)):
		temp = rectangle[index]
		canvas.itemconfigure(temp, text = grid[adjIndex], font = 'Courier 36')
		adjacent = rectangle[adjIndex]
		canvas.itemconfigure(adjacent, text = grid[index], font = 'Courier 36')
		temp2 = grid[index] #swap
		grid[index] = grid[adjIndex] #swap
		grid[adjIndex] = temp2 #swap
	canvas.itemconfigure(display[0], text = heuristic1(), font = 'Courier 48')
	canvas.itemconfigure(display[1], text = heuristic2(), font = 'Courier 48')

def shuffleBoard():
	global grid, rectangle
	count = 0
	shuffle(grid)
	for count in range(len(rectangle)):
		canvas.itemconfigure(rectangle[count], text = grid[count], font = 'Courier 36')
	return rectangle


def heuristic1(): #Number of Tiles Out Of Place
	global grid
	count = 0
	temp = 1
	for temp in range(len(grid)):
		if grid[-1] == '' and temp == len(grid)-1: #accounts for blank square
			count = count + 1
		elif temp == grid[temp-1]:
			count = count +1 
	return len(grid)-count-1

def heuristic2(): #Manhattan Distance
	global grid
	leng = int(sqrt(len(grid)))
	manhattan = 0
	for temp in range(len(grid)):
		if grid[temp] == "":
			continue
		else:
			xcur = (grid[temp]-1)/leng
			ycur = (grid[temp]-1)%leng
			xfin = (temp)/leng
			yfin = (temp)%leng
			manhattanx = fabs(xcur - xfin)
			manhattany = fabs(ycur - yfin)
			manhattan+= (manhattanx + manhattany)
    return manhattan

def quit(evnt):
	exit(0)

canvas.pack()
objt=canvas.create_text(x+dx/2,y+dy/2,text='Bye!',fill='white')
row, col = 0, 0
num = 1
while row < 4:
	while col < 4:
		rect = canvas.create_rectangle(x, y, x+dx, y+dy, fill = 'white', outline = 'black')
		objt = canvas.create_text(x+dx/2, y+dy/2, text= num, font = 'Courier 36', fill = 'black')
		grid.append(num)
		rectangle.append(objt)
		col=col+1
		x = x + dx
		num=num+1
	row=row+1
	col = 0
	y = y+ dy
	x = 75
  
temp = rectangle[-1]
grid[-1] = ''
canvas.itemconfigure(temp, text = '', font = 'Courier 48')
head1 = canvas.create_text(800, 100, text = 'Tiles out of Place', font = 'Courier 24', fill = 'black')
disp1 = canvas.create_text(800, 200, text = '0', font = 'Courier 48', fill = 'black')
head2 = canvas.create_text(800, 500, text = 'Manhattan Distance', font = 'Courier 24', fill = 'black')
disp2 = canvas.create_text(800, 600, text = '0', font = 'Courier 48', fill = 'black')
print heuristic2()
display.append(disp1)
display.append(disp2)
      
      
root.bind('<Button-1>',click)
root.bind('<q>',quit)
root.mainloop()