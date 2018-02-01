# Now make a square rotate continuously, one full revolution (360 degrees) per second

# To increase orientation use `square.ori += value` where `value` is the value by which to increase the orientation.

import time
import sys
from psychopy import visual,event,core

# Show a red square for 1s then change its orientation by 45 degrees
time = 1/360
win = visual.Window([400,400],color="black", units='pix')  # make a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) # make a square!
square.draw() # draw it on the buffer
win.flip() # show it!
core.wait(1) # let it show for 1.5 seconds

for num in range (360):
	square.ori += 1
	square.draw()
	win.flip() 
	core.wait(time) 
	
core.wait(1)
sys.exit()