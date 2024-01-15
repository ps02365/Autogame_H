import pyautogui
from time import sleep
import keyboard

pyautogui.FAILSAFE = False

def ent17gs():
    sleep(0.05)
    pyautogui.doubleClick(button="left",x=1034,y=712) #Sub
    sleep(0.05)
    pyautogui.doubleClick(button="left",x=1065,y=712) #ProtectEnt
    sleep(0.05)
    pyautogui.doubleClick(button="left",x=1100,y=712) #Weapon
    sleep(0.05)
    pyautogui.leftClick(1270, 687)
    sleep(2)
    pyautogui.leftClick(1270, 687)

def ent16():
    sleep(0.05)
    pyautogui.doubleClick(button="left",x=1000,y=712) #Sub
    sleep(0.05)
    pyautogui.doubleClick(button="left",x=1065,y=712) #ProtectEnt
    sleep(0.05)
    pyautogui.doubleClick(button="left",x=1100,y=712) #Weapon
    sleep(0.05)
    pyautogui.leftClick(1270, 687)
    sleep(2)
    pyautogui.leftClick(1270, 687)

def hotkey_ent17gs():
    ent17gs()

def hotkey_ent16():
    ent16

keyboard.add_hotkey("num 1", hotkey_ent16)
keyboard.add_hotkey("num 2", hotkey_ent17gs)
keyboard.wait()