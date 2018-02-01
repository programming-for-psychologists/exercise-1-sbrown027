import time
import sys
from psychopy import visual,event,core

# Show a red square for 1s then change its orientation by 45 degrees

win = visual.Window([400,400],color="black", units='pix')  # make a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) # make a square!
square.draw() # draw it on the buffer
win.flip() # show it!
core.wait(1) # let it show for 1.5 seconds
square.setOri(45) 
core.wait(1) # hide for 1 second