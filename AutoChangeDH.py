import win32gui
import time
import pydirectinput
import pyautogui
import keyboard
import tkinter as tk

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False


def focus_dream_ace():
    hwnd = win32gui.FindWindow(None, "DreamACE")
    if not hwnd:
        raise Exception("Not found DreamACE window")
    win32gui.SetForegroundWindow(hwnd)

def X_form():
    # pyautogui.keyDown('r')
    # time.sleep(0.01)
    pyautogui.click(button='left',x=253,y=1041) #change chat channel
    # time.sleep(0.001)
    pyautogui.click(button='left',x=395,y=1067) #open F7
    # time.sleep(0.001)
    pyautogui.click(button='left',x=804,y=558) #Choose flight form list
    # time.sleep(0.001)
    pyautogui.click(button='left',x=740,y=712) #Choose flight form "X"
    # time.sleep(0.001)    
    pyautogui.click(button='left',x=988,y=725) #Apply
    # time.sleep(0.001)
    pyautogui.click(button='left',x=21,y=1040) #All chat channel
    # time.sleep(0.001)
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    # time.sleep(0.001)
    keyupR()
    # time.sleep(0.001)
    pyautogui.press('esc') #Exit F7


def Boost_form():
    # pyautogui.keyDown('r')
    # time.sleep(0.01)
    pyautogui.click(button='left',x=253,y=1041) #change chat channel
    # time.sleep(0.001)
    pyautogui.click(button='left',x=395,y=1067) #open F7
    # time.sleep(0.001)
    pyautogui.click(button='left',x=804,y=558) #Choose flight form list
    # time.sleep(0.001)
    pyautogui.click(button='left',x=740,y=598) #Choose flight form "Boost"
    # time.sleep(0.001)    
    pyautogui.click(button='left',x=988,y=725) #Apply
    # time.sleep(0.001)
    pyautogui.click(button='left',x=21,y=1040) #All chat channel
    # time.sleep(0.001)
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    # time.sleep(0.001)
    keyupR()
    # time.sleep(0.001)
    pyautogui.press('esc') #Exit F7

def ChangeLeader():
    pyautogui.click(button='left',x=253,y=1041) #change chat channel
    # time.sleep(0.001)
    pyautogui.click(button='left',x=395,y=1067) #open F7
    # time.sleep(0.001) 
    pyautogui.click(button='left',x=21,y=1040) #All chat channel
    # time.sleep(0.001) 
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    # time.sleep(0.001)
    keyupR()

# def DHexit():
      #root.destroy()
#     exit()

def keydownR():
    time.sleep(0.05)
    pydirectinput.keyDown('r')
    # time.sleep(0.001)

def keyupR():
    pydirectinput.keyUp('r')

def hotkey_X():
    keydownR()
    X_form()
    # keyupR()

def hotkey_Boost():
    keydownR()
    Boost_form()
    # keyupR()

def hotkey_changeLeader():
    keydownR()
    ChangeLeader()
    # keyupR()

# def hotkey_exit():
#     DHexit()

# root = tk.Tk()
# root.title ="AutoChangeDH"

# button1 = tk.Button(root, text="X", command=X_form)
# button1.pack(pady=10)

# button2 = tk.Button(root, text="B", command=Boost_form)
# button2.pack(pady=10)

# button3 = tk.Button(root, text="Exit", command=DHexit)
# button3.pack(pady=10)


keyboard.add_hotkey('space+1', hotkey_X)
keyboard.add_hotkey('space+2', hotkey_Boost)
keyboard.add_hotkey('space+3', hotkey_changeLeader)
# keyboard.add_hotkey('ctrl+E', hotkey_exit)
keyboard.wait()
# root.mainloop()
