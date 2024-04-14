from time import sleep
import pyautogui
import keyboard
import win32gui
import pydirectinput
import sys
import signal
from threading import Thread

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False

powered_by =r"""
  __     __  ___       ____       ___  _____    __   _________  
 |  |   |  | \  \     /    \     /  / |     \  |  | |   ______|  
 |  |___|  |  \  \   /  /\  \   /  /  |  |\  \ |  | |  |  ____  
 |   ___   |   \  \ /  /  \  \ /  /   |  | \  \|  | |  | |_   | 
 |  |   |  |    \  V  /    \  V  /    |  |  \  \  | |  |___|  | 
 |__|   |__|     \___/      \___/     |__|   \____| |_________| 

"""
running = True
change_form_enable = False     

def trigger_change_form_status():
    global change_form_enable
    change_form_enable = not change_form_enable
    if not change_form_enable:
        pydirectinput.keyDown('esc')
        sleep(0.1)
        pydirectinput.keyUp('esc')
        sleep(0.1)
        # pydirectinput.keyDown('r')
        # sleep(0.1)
        # pydirectinput.keyUp('r')
        # sleep(0.1)
        print('\nKhông cho phép đổi đội hình')
        return
    pydirectinput.keyDown('esc')
    sleep(0.1)
    pydirectinput.keyUp('esc')
    sleep(0.1)
    pydirectinput.keyDown('r')
    sleep(0.05)
    pydirectinput.keyUp('r')
    sleep(0.05)
    print('\nCho phép đổi đội hình')           
    # pydirectinput.keyDown('r')
    # sleep(0.1)
    # pydirectinput.keyUp('r')
    # sleep(0.1)

def signal_handler(sig, frame):
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)

def auto_ammunition():
    while True:
        if running:
            use_ammunition_box()   
        sleep(1)

def use_ammunition_box():
    left = 0     
    top = 0
    width = 350
    height = 50
    region_to_fetch = (left,top,width,height)   
    try:
        ammunition = pyautogui.locateOnScreen('./1920x1080/out_of_ammunition.png', region = region_to_fetch, confidence=0.7, grayscale= False)
    except:
        ammunition = None
    if ammunition:
        sleep(0.1)
        pydirectinput.press("8")
        sleep(0.1)

def X_form():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=837,y=552) #Choose flight form list
    pyautogui.click(button='left',x=781,y=676) #Choose flight form "X"   
    pyautogui.click(button='left',x=980,y=690) #Apply
    pyautogui.click(button='left',x=16,y=1050) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()
    pyautogui.press('esc') #Exit F7

def Boost_form():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=837,y=552) #Choose flight form list
    pyautogui.click(button='left',x=777,y=590) #Choose flight form "Boost"  
    pyautogui.click(button='left',x=980,y=690) #Apply
    pyautogui.click(button='left',x=16,y=1050) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()
    pyautogui.press('esc') #Exit F7

def Zero_form():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=837,y=552) #Choose flight form list
    pyautogui.click(button='left',x=774,y=631) #Choose flight form "Zero"  
    pyautogui.click(button='left',x=980,y=690) #Apply
    pyautogui.click(button='left',x=16,y=1050) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()
    pyautogui.press('esc') #Exit F7

def ChangeLeader():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=1050) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()

def keydownR():
    pydirectinput.keyDown('r')

def keyupR():
    pydirectinput.keyUp('r')

def hotkey_X():
    if not change_form_enable:
        return
    keydownR()
    X_form()

def hotkey_Boost():
    if not change_form_enable:
        return
    keydownR()
    Boost_form()

def hotkey_Zero():
    if not change_form_enable:
        return
    keydownR()
    Zero_form()
    
def hotkey_changeLeader():
    if not change_form_enable:
        return
    keydownR()
    ChangeLeader()

if __name__ == "__main__":
    print (powered_by)
    print ("Powered by Hwng")
    sleep(0.05)
    print ("\nHướng dẫn đổi đội hình\nF1 để kích hoạt\n    Space + Z = Giao diện đội hình\n    Space + C = Chia damage\n    Space + V = Tăng tốc\n    Space + X = 0ms\nSpace + ALT để tắt")
    sleep(0.05)
    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()
    print('\nKích hoạt tự động nạp đạn')
    sleep(0.05)
    # input("\nBấm Enter để trở về game!")
    # sleep(0.05)
    print('\nBắt đầu')
    sleep(0.05)
    hwd = win32gui.FindWindow(None, "DreamACE")
    if not hwd:
        print ('\nKhông tìm thấy game.')
        sleep(1)
        print ('\nThoát phần mềm trong 2 giấy.')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)
        exit()
    win32gui.SetForegroundWindow(hwd)
    keyboard.add_hotkey('F1',trigger_change_form_status)    
    keyboard.add_hotkey('space+c', hotkey_X)
    keyboard.add_hotkey('space+v', hotkey_Boost)
    keyboard.add_hotkey('space+x', hotkey_Zero)
    keyboard.add_hotkey('space+z', hotkey_changeLeader)
    keyboard.add_hotkey('space+alt', signal.raise_signal, args=(signal.SIGINT,))
    keyboard.wait()