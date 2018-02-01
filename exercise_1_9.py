# Make a square stop rotating when you press 's' and then start rotating again when you press 'r'



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

# isRotating = True

# while True:
# 	if isRotating:
# 		square.ori += 1
# 		square.draw()
# 		win.flip() 
# 		core.wait(time)
# 		if event.getKeys(['s']):
# 			isRotating = False
# 	else:
# 		if event.getKeys(['r']):
# 			isRotating = True

while True:
	square.ori += 1
	square.draw()
	win.flip() 
	core.wait(time)
	if event.getKeys(['s']):
		break


while True:
	if event.getKeys(['r']):
		while True:
			square.ori += 1
			square.draw()
			win.flip() 
			core.wait(time)
			if event.getKeys(['s']):
				sys.exit()

sys.exit()

