import pyautogui
from time import sleep
import win32gui
'''
MouseClick($MOUSE_CLICK_LEFT, 1166,623, 2 , 1)
Sleep(10)
MouseMove(1166,623)
Sleep(10)
MouseClick($MOUSE_CLICK_LEFT, 1326, 982, 2, 1)
'''
hwnd = win32gui.FindWindow(None, "DreamACE")
if not hwnd:
    raise Exception("Not found DreamACE window")
win32gui.SetForegroundWindow(hwnd)
while True:
    pyautogui.leftClick(1166,623)
    sleep(0.1)
    pyautogui.leftClick(1326, 982)
    sleep(3)