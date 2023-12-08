import pyautogui
from time import sleep
import win32gui
import pydirectinput

hwnd = win32gui.FindWindow(None, "DreamACE")
if not hwnd:
    raise Exception("Not found DreamACE window")
win32gui.SetForegroundWindow(hwnd)
while True:
    # pydirectinput.press("3")
    # sleep(0.01)
    pydirectinput.press("4")
    sleep(0.01)