#
# Torbert, 10.8.2008
#
# Tkinter Demo, Version 1.0
#
#   Input: none
# Process: a square with a message tries to run off the screen
#  Output: graphical display updated every 10 milliseconds
#

from Tkinter import *
from sys import exit

w,h=800,600
x,y,dx,dy=100,50,175,175

def tick():
	global x
	x+=1
#	x1,y1,x2,y2=canvas.coords(rect)
#	print x1,y1,x2,y2
	print canvas.itemcget(objt,'text')
	canvas.coords(rect,x,y,x+dx,y+dy) # move the objects
	canvas.coords(objt,x+dx/2,y+dy/2)
	canvas.after(10,tick) # animation

def click(evnt):
	global x,y
	x,y=evnt.x,evnt.y
	canvas.itemconfigure(objt,text='Hey!',font='Courier 48')

def quit(evnt):
	exit(0)

#
# Initialize.
#
root=Tk()
canvas=Canvas(root,width=w,height=h,bg='white')
canvas.pack()
#
# Graphics objects. 
#
rect=canvas.create_rectangle(x,y,x+dx,y+dy,fill='black',outline='black')
objt=canvas.create_text(x+dx/2,y+dy/2,text='Bye!',fill='white')
#
# Callbacks.
#
root.bind('<Button-1>',click)
root.bind('<q>',quit)
canvas.after(10,tick) # animation
#
# Here we go.
#
root.mainloop()
