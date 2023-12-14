import win32gui
import time
import pydirectinput
import pyautogui
import keyboard
import tkinter as tk

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False

def X_form():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=837,y=552) #Choose flight form list
    pyautogui.click(button='left',x=781,y=676) #Choose flight form "X"   
    pyautogui.click(button='left',x=980,y=690) #Apply
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()
    pyautogui.press('esc') #Exit F7

def Boost_form():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=837,y=552) #Choose flight form list
    pyautogui.click(button='left',x=777,y=590) #Choose flight form "Boost"  
    pyautogui.click(button='left',x=980,y=690) #Apply
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()
    pyautogui.press('esc') #Exit F7

def ChangeLeader():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()

def ChangeLeaderSlot1():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    keyupR()
def ChangeLeaderSlot2():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7 
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    keyupR()

def ChangeLeaderSlot3():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    keyupR()
def ChangeLeaderSlot4():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    keyupR()

def ChangeLeaderSlot5():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    keyupR()

def ChangeLeaderSlot6():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=690) #All chat channel
    keyupR()

def keydownR():
    time.sleep(0.05)
    pydirectinput.keyDown('r')

def keyupR():
    pydirectinput.keyUp('r')

def hotkey_X():
    keydownR()
    X_form()

def hotkey_Boost():
    keydownR()
    Boost_form()

def hotkey_changeLeader():
    keydownR()
    ChangeLeader()

def hotkey_change_leader_slot1():
    keydownR()
    ChangeLeaderSlot1()

def hotkey_change_leader_slot2():
    keydownR()
    ChangeLeaderSlot2()

def hotkey_change_leader_slot3():
    keydownR()
    ChangeLeaderSlot3()

def hotkey_change_leader_slot4():
    keydownR()
    ChangeLeaderSlot4()

def hotkey_change_leader_slot5():
    keydownR()
    ChangeLeaderSlot5()

def hotkey_change_leader_slot6():
    keydownR()
    ChangeLeaderSlot6()

keyboard.add_hotkey('space+c', hotkey_X)
keyboard.add_hotkey('space+v', hotkey_Boost)
keyboard.add_hotkey('space+x', hotkey_changeLeader)
keyboard.add_hotkey('Num1', hotkey_change_leader_slot1)
keyboard.add_hotkey('Num2', hotkey_change_leader_slot2)
keyboard.add_hotkey('Num3', hotkey_change_leader_slot3)
keyboard.add_hotkey('Num4', hotkey_change_leader_slot4)
keyboard.add_hotkey('Num5', hotkey_change_leader_slot5)
keyboard.add_hotkey('Num6', hotkey_change_leader_slot6)
keyboard.wait()

