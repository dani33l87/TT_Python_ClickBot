"""
All coordinates assume a screen resolution of 1366x7680 and a Firefox browser.
This is a basic click bot.
x_pad = 185
y_pad = 230
Play area =  x_pad+1, y_pad+1, 975, 510
"""

import win32api, win32con
from PIL import ImageGrab
import os
import time


os.system('C:\Progra~2\Mozill~1\Firefox.exe http://www.bing.com/search?q=Fatal+Car+crash%2C+incredible+accident&go=&qs=n&form=QBRE&filt=all'); 
time.sleep(3.1)

# Globals
# ------------------
 
x_pad = 185
y_pad = 230

def screenGrab():
    box = (x_pad+1, y_pad+1,x_pad+975, y_pad+510)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
  
def main():
    screenGrab()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."          #completely optional. But nice for debugging purposes.  

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y
                         
def clickbot():
    #location of first menu
    print "clickbot()"
    mousePos((78, 247))
    leftClick()
    time.sleep(3.1)
     
    #location of second menu
    mousePos((729, 171))
    leftClick()
    time.sleep(3.1)
     
    #location of third menu
    mousePos((138, 91))
    leftClick()
    time.sleep(3.1)
     
    #location of fourth menu
    mousePos((748, 295))
    leftClick()
    time.sleep(3.1)


clickbot()


if __name__ == '__main__':
    pass
