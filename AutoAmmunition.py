import pyautogui
import pydirectinput
from time import sleep
import win32gui


f = open("config.txt", "r")
config_params = f.read().split('\n')
ammunition_key = config_params[0].split('=')[1]
confidence_point = config_params[1].split('=')[1]

def auto_ammunition():
    while True:
        use_ammunition_box()
        sleep(0.05)

def use_ammunition_box():
    ammunition = pyautogui.locateOnScreen('out_of_ammunition.png', region=(0, 0, 300, 100), confidence=confidence_point)
    if ammunition:
        sleep(0.1)
        pydirectinput.press(ammunition_key)
        sleep(0.1)

if __name__ == '__main__':
    print("--------Auto Ammunition--------")
    
    hwnd = win32gui.FindWindow(None, "DreamACE")
    if not hwnd:
        raise Exception("Not found DreamACE window")
    win32gui.SetForegroundWindow(hwnd)
    sleep(1)
    auto_ammunition()
