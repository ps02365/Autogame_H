import win32gui
import time
import pydirectinput
import pyautogui

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False

def X_form():
    pyautogui.keyDown('r')
    time.sleep(0.05)
    pyautogui.click(button='left',x=0,y=0) #change chat channel
    time.sleep(0.05)
    pyautogui.click(button='left',x=0,y=0) #open F7
    time.sleep(0.05)
    pyautogui.click(button='left',x=0,y=0) #Choose flight form list
    time.sleep(0.05)
    pyautogui.click(button='left',x=0,y=0) #Choose flight form
    time.sleep(0.05)    
    pyautogui.click(button='left',x=0,y=0) #Apply
    time.sleep(0.05)
    pyautogui.keyUp('r')
    time.sleep(0.05)
    pyautogui.press('esc') #Exit F7
    time.sleep(0.05) 

if __name__ == "__main__":



