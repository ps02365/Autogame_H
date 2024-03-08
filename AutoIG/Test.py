from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw


pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False


def start_game():
    gw.getWindowsWithTitle('DreamACE')[0].activate()
    sleep(1)

    start_auto()


def start_auto():
    screenshot()

def screenshot():
    right = 1889     
    top = 252
    width = 19
    height = 63
    region_to_fetch = (right,top,width,height)
    pyautogui.screenshot("Test_screenshot.png",region_to_fetch) 

def no_cd():
    pyautogui.mouseDown(button='left')
    sleep(0.2)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseDown(button='left')
    
start_game()