import time
import sys
from psychopy import visual,event,core
 
# Make the square appear for 1.5 secs, then show a blank screen for 1 sec, then flash the square 3 times for 30 ms each.


win = visual.Window([400,400],color="black", units='pix')  # make a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) # make a square!
square.draw() # draw it on the buffer
win.flip() # show it!
core.wait(1.5) # let it show for 1.5 seconds
win.flip() # hide it
core.wait(1) # hide for 1 second

for num in range(3):
	square.draw() # redraw
	win.flip() # show
	core.wait(.3) # flash #1
	win.flip() # hide
	core.wait(.3) # hide for a little 


sys.exit()

