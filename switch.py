"""
 
All coordinates assume a screen resolution of 1366x7680 and a Firefox browser.
Also to work you need to use the add-on firefox Elite Proxy Switcher.
If you hae all the request this is supose to work.

x_pad = 185
y_pad = 230
Play area =  x_pad+1, y_pad+1, 975, 510
"""
import win32api, win32con
from PIL import ImageGrab
import os
import time

os.system('C:\Progra~2\Mozill~1\Firefox.exe http://www.hidemyass.com/proxy-list/'); 
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

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

def options():

    #roll position
    mousePos((1171, -65))
    leftDown()
    time.sleep(0.5)
     
    #roll final position
    mousePos((1171, -9))
    leftUp()
    time.sleep(0.5)

    mousePos((497, 187))
    leftClick()
    time.sleep(0.5)

    mousePos((612, 149))
    leftClick()
    time.sleep(0.5)

    mousePos((612, 166))
    leftClick()
    time.sleep(0.5)

    mousePos((612, 184))
    leftClick()
    time.sleep(0.5)

    mousePos((612, 205))
    leftClick()
    time.sleep(0.5)

    mousePos((612, 274))
    leftClick()
    time.sleep(0.5)

    mousePos((765, 150))
    leftClick()
    time.sleep(0.5)

    mousePos((765, 167))
    leftClick()
    time.sleep(0.5)

    mousePos((765, 236))
    leftClick()
    time.sleep(0.5)

    mousePos((765, 256))
    leftClick()
    time.sleep(0.5)

    mousePos((386, 337))
    leftClick()
    time.sleep(0.5)

    mousePos((338, 357))
    leftClick()
    time.sleep(0.5)

    mousePos((860, 332))
    leftClick()
    time.sleep(3.5) 

options()

def roll():
 
    #roll position
    mousePos((1171, -65))
    leftDown()
    time.sleep(0.5)
     
    #roll final position
    mousePos((1171, 162))
    leftUp()
    time.sleep(0.5)
    
    #select ip
    mousePos((137, 155))
    leftDown()
    time.sleep(0.5)
     
    #select ip all
    mousePos((250, 155))
    leftUp()
    time.sleep(0.5)
    
    #select copy 
    mousePos((189, 155))
    rightClick()
    time.sleep(0.5)
     
    #copy is done
    mousePos((241, 167))
    leftClick()
    time.sleep(0.5)

    #open switch
    mousePos((1069, 496))
    rightClick()
    time.sleep(0.5)

    #change to manual proxy
    mousePos((868, 279))
    leftClick()
    time.sleep(0.5)

    #select area ip
    mousePos((923, 305))
    leftDown()
    time.sleep(0.5)
     
    #select all ip area
    mousePos((1035, 305))
    leftUp()
    time.sleep(0.5)

    #click right area ip
    mousePos((975, 305))
    rightClick()
    time.sleep(0.5)

    #paste ip proxy
    mousePos((1025, 390))
    leftClick()
    time.sleep(0.5)

    #OK proxy
    mousePos((1011, 450))
    leftClick()
    time.sleep(0.5)

    #select port
    mousePos((277, 155))
    leftDown()
    time.sleep(0.5)
     
    #select port all
    mousePos((315, 155))
    leftUp()
    time.sleep(0.5)
    
    #select copy 
    mousePos((295, 155))
    rightClick()
    time.sleep(0.5)
     
    #copy is done
    mousePos((357, 166))
    leftClick()
    time.sleep(0.5)

    #open switch
    mousePos((1069, 496))
    rightClick()
    time.sleep(0.5)

    #select area port
    mousePos((1118, 305))
    leftDown()
    time.sleep(0.5)
     
    #select all port area
    mousePos((1088, 305))
    leftUp()
    time.sleep(4.1)

    #click right area port
    mousePos((1105, 305))
    rightClick()
    time.sleep(0.5)

    #paste port proxy
    mousePos((1107, 390))
    leftClick()
    time.sleep(0.5)

    #OK proxy
    mousePos((1011, 450))
    leftClick()
    time.sleep(0.5)

roll()                         


if __name__ == '__main__':
    pass

