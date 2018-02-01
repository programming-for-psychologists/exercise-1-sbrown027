import time
import sys
from psychopy import visual,event,core

#Show the following sequence: blue, red, blue, red, blue, red (with each square appearing for 1 s with a 50 ms blank screen in the middle).

win = visual.Window([400,400],color="black", units='pix')  # make a window
squareRed = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) # make a RED square!
squareBlue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100]) # make a RED square!


for num in range(6):
	if num % 2 == 0:
		squareBlue.draw() # redraw
	else:
		squareRed.draw() # redraw
	win.flip() # show
	core.wait(1) # flash #1
	win.flip() # hide
	core.wait(.5) # hide for a little 


sys.exit()