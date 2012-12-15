"""
All coordinates assume a screen resolution of 1366x7680 and a Firefox browser.
You need to change all the coordanates, this are special made for my os.
x_pad = 0
y_pad = 0
Play area =  x_pad+1, y_pad+1, 1100, 700
"""

import win32api, win32con
from PIL import ImageGrab
import os
import time


# Globals
# ------------------
 
x_pad = 0
y_pad = 0

def screenGrab():
    box = (x_pad+1, y_pad+1,x_pad+1100, y_pad+700)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
  
def main():
    screenGrab()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y
                         
def cookie():
    
    #disable switch
    mousePos((1243, 726))
    leftClick()
    time.sleep(1.1)
    
    #location of first menu
    mousePos((65, 8))
    leftClick()
    time.sleep(1.5)
     
    #location of second menu
    mousePos((247, 139))
    leftClick()
    time.sleep(1.5)
     
    #location of third menu
    mousePos((418, 400))
    leftClick()
    time.sleep(1.5)
     
    #location of fourth menu
    mousePos((559, 511))
    leftClick()
    time.sleep(1.5)

    #location of five menu
    mousePos((530, 571))
    leftClick()
    time.sleep(1.5)
    
    #location of six menu
    mousePos((1337, 6))
    leftClick()
    time.sleep(1.5)

cookie()


if __name__ == '__main__':
    pass

