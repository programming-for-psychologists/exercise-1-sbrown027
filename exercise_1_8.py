# Make a rotating square stop rotating when you press the 's' key

# To accept keyboard input you'll want to check it event.getKeys(['s']) is True.


import time
import sys
from psychopy import visual,event,core

# Show a red square for 1s then change its orientation by 45 degrees
time = 1/360

win = visual.Window([400,400],color="black", units='pix')  # make a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) # make a square!
square.draw() # draw it on the buffer
win.flip() # show it!
core.wait(1) # let it show for 1 seconds

while True:
	square.ori += 1
	square.draw()
	win.flip() 
	core.wait(time)
	if event.getKeys(['s']) == ['s']:
		break

sys.exit()

