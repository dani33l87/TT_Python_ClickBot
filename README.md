TT_Python_ClickBot
==================



-----------
Introduction
____________



*** What is a click bot?

“A clickbot is a software program that can simulate the clicking of different ads on any Web page,
at any URL, at predetermined, random time intervals, whilst showing a different origin IP address
each time. A well-written clickbot can be worth a fortune.”

*** It`s that legal?


“ In 2004, a California man created a clickbot that he claimed cannot be detected by Google. Failed
to make good money selling the program, he tried to blackmail Google for $150,000 to hand over the
program. He was arrested, nonetheless.”


*** Build a Click Bot

You can build your own click bot to play online games automatic without spending your time to do the same boring actions,
practically you can use a click bot to automatize any kind of mechanic action.


The python script available on the github repository was made in Python 2.7 using a screen resolution
of 1366x768 and a Firefox browser. This is important in order to test the code.

*** Requirements:

Python 2.7: http://www.python.org/getit/

IDLE: http://docs.python.org/2/library/idle.html

Paint.net: http://www.getpaint.net/

Python Imaging Library : http://www.pythonware.com/products/pil/

Numpy: http://numpy.scipy.org/

PyWin: http://sourceforge.net/projects/pywin32/


Script Structure
================

In order to make it easy for debugging is better to split the click bot script in different parts, like: script for 
deleting the cookies, script to switch proxy, the actual click bot action (create different random situation, 
changing the cover source).  

In this why if something is not working you can go directly to problem script and fix it.
For that the execution script will only lead to execute the other scripts in the order request.

You can see a clear example in my code. Every script has an action and if something is going wrong I will go to that
script and fix it without being annoying for the rest of code on testing.


Short Tutorial
==============
  
In order to make it work you need to create a screen grab and get the coordinates base on your play area.
To do that you`ll learn that get_coors() is a very nice tool, you only need to position the mouse to 
the desire place before to action the get_cords function.

All the code is made using coordinate and some os library in order to open Firefox.

In order to be able to use right click and left click you need to use this functions:


------------------------------------------------------------
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def rightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    
------------------------------------------------------------
    
With this you can make your mouse to act as a real one, taking full advantages of the all mouse options.
We can find the full code in the switch.py file, where the mouse is used to roll the page and also select and copy
a piece of text.

After you understand the basic you can automated any actions of your using coordinates and python.


Tip
====

*** To understanding better how everthing works I recommend you to follow this nice tutorial, that explain every well
and also give a good exemple how can you create a bot game.

http://active.tutsplus.com/tutorials/workflow/how-to-build-a-python-bot-that-can-play-web-games/
