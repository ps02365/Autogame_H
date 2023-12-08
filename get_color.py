import win32gui
import pyautogui
import time
from PIL import Image
import easyocr

region = (838,1046, 25, 12)

hwnd = win32gui.FindWindow(None, "DreamACE")
if not hwnd:
    raise Exception("Not found DreamACE window")

while True:
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    pyautogui.screenshot('my_screenshot.png', region=region)

    time.sleep(1)

    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext('my_screenshot.png', decoder="greedy", batch_size=6, allowlist="1234567890",detail=0, low_text=0.3)
    print(result)
    time.sleep(1)

