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
roll_enable = False

def trigger_change_roll_status():
    global roll_enable
    roll_enable = not roll_enable
    if not roll_enable:
        pydirectinput.keyDown('r')
        sleep(0.1)
        pydirectinput.keyUp('r')
        sleep(0.1)
        print('\nKhông cho phép roll')
        return
    pydirectinput.keyDown('r')
    sleep(0.1)
    pydirectinput.keyUp('r')
    sleep(0.1)
    print('\nCho phép roll')           

def trigger_change_form_status():
    global change_form_enable
    change_form_enable = not change_form_enable
    if not change_form_enable:
        pydirectinput.keyDown('r')
        sleep(0.1)
        pydirectinput.keyUp('r')
        sleep(0.1)
        print('\nKhông cho phép đổi đội hình')
        return
    pydirectinput.keyDown('r')
    sleep(0.1)
    pydirectinput.keyUp('r')
    sleep(0.1)
    print('\nCho phép đổi đội hình')           

def signal_handler(sig, frame):
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)

def auto_ammunition():
    while True:
        if running:
            use_ammunition_box()
        sleep(0.02)

def use_ammunition_box():
    try:
        ammunition = pyautogui.locateOnScreen('./1920x1080/out_of_ammunition.png', confidence=0.6, grayscale= False)
    except:
        ammunition = None
    if ammunition:
        sleep(0.1)
        pydirectinput.press("8")
        sleep(0.1)

def locate_image_tick():
    left = 640     
    top = 432
    width = 640
    height = 216
    region_to_fetch = (left,top,width,height)
    try:
        tick = pyautogui.locateOnScreen('./1920x1080/tick.png', region=region_to_fetch, confidence=0.6,grayscale=False)
        if tick is not None:
            return tick
    except Exception as e:
        print("Not Found Tick", e)
        return Not_Found_Tick()
    
def locate_image_arrange():
    left = 900     
    top = 650
    width = 300
    height = 220
    region_to_fetch = (left,top,width,height)
    try:
        inventory = pyautogui.locateOnScreen('./1920x1080/arrange.png',region=region_to_fetch, confidence=0.7,grayscale=False)
        if inventory is not None:
            return inventory
    except Exception as e:
        print("Not Found Arrange", e)
        return Not_Found_Arrange()

def Not_Found_Tick():
    pydirectinput.keyDown("esc")    
    sleep(0.05)
    pydirectinput.keyUp("esc")  
    sleep(0.05)
    pydirectinput.keyDown("b")    
    sleep(0.05)
    pydirectinput.keyUp("b")
    sleep(0.05)
    locate_image_tick()   

def Not_Found_Arrange():
    pydirectinput.keyDown("esc")    
    sleep(0.05)
    pydirectinput.keyUp("esc")  
    sleep(0.05)
    pydirectinput.keyDown("i")    
    sleep(0.05)
    pydirectinput.keyUp("i")
    sleep(0.05)
    locate_image_arrange()

def Stop():
    sleep(0.05)
    pydirectinput.keyDown('b')
    sleep(0.05)
    pydirectinput.keyUp('b')
    sleep(0.05)
    image_position_tick = locate_image_tick()
    if image_position_tick:
        left, top, width, height = image_position_tick
    pyautogui.click(left+15,top+20) 
    sleep(0.05)
    pydirectinput.keyDown("i")    
    sleep(0.05)
    pydirectinput.keyUp("i")  
    
def Accuracy():
    if not roll_enable:
        return    
    Stop()
    sleep(0.05)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll CX')
        left, top, width, height = image_position_inventory 
    pyautogui.doubleClick(left-270,top-225)
    pyautogui.doubleClick(left-300,top-225)
    sleep(0.05)
    pyautogui.doubleClick(left-300,top-225)
    pyautogui.doubleClick(left-300,top-225)
    sleep(0.05)
    pyautogui.doubleClick(left-300,top-200)
    pyautogui.doubleClick(left-300,top-200)
    sleep(0.05)
    pyautogui.doubleClick(left-270,top-200)
    pyautogui.doubleClick(left-270,top-200)  
    sleep(0.05)
    pydirectinput.keyDown('c')
    sleep(0.05)
    pydirectinput.keyUp('c')

def Accuracy_VIP():
    if not roll_enable:
        return    
    Stop()
    sleep(0.05)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll CX')
        left, top, width, height = image_position_inventory 
    pyautogui.doubleClick(left-10,top-300)
    sleep(0.05)
    pyautogui.doubleClick(left-270,top-200) 
    sleep(0.05)
    pydirectinput.keyDown('c')
    sleep(0.05)
    pydirectinput.keyUp('c')    

def Pierce():
    if not roll_enable:
        return   
    Stop()
    sleep(0.05)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll XP')
        left, top, width, height = image_position_inventory 
    pyautogui.doubleClick(left-170,top-225)
    sleep(0.12)
    pyautogui.doubleClick(left-200,top-225)
    sleep(0.12)
    pyautogui.doubleClick(left-200,top-200)
    sleep(0.12)
    pyautogui.doubleClick(left-170,top-200) 
    sleep(0.05)
    pydirectinput.keyDown('c')
    sleep(0.05)
    pydirectinput.keyUp('c')

def Pierce_VIP():
    if not roll_enable:
        return   
    Stop()
    sleep(0.05)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll XP')
        left, top, width, height = image_position_inventory 
    pyautogui.doubleClick(left,top-300)
    sleep(0.05)
    pyautogui.doubleClick(left-200,top-200)
    sleep(0.05)
    pydirectinput.keyDown('c')
    sleep(0.05)
    pydirectinput.keyUp('c') 

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
    sleep(0.5)
    print ("\nHướng dẫn đổi đội hình\nSpace + Ctrl để kích hoạt\n    Space + C = Chia damage\n    Space + V = Tăng tốc\n    Space + X = 0ms\nSpace + ESC để tắt")
    sleep(0.5)
    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()
    print('\nKích hoạt tự động nạp đạn')
    sleep(0.5)
    input("\nBấm Enter để trở về game!")
    sleep(0.5)
    print('\nBắt đầu')
    sleep(0.5)
    hwd = win32gui.FindWindow(None, "DreamACE")
    if not hwd:
        print ('\nKhông tìm thấy game.')
        sleep(1)
        print ('Thoát phần mềm trong 2 giấy.')
        sleep(2)
        exit()
    win32gui.SetForegroundWindow(hwd)
    keyboard.add_hotkey('ctrl+alt',trigger_change_roll_status)
    keyboard.add_hotkey('ctrl+x',Pierce)
    keyboard.add_hotkey('ctrl+z',Accuracy)
    keyboard.add_hotkey('ctrl+space',trigger_change_form_status)    
    keyboard.add_hotkey('space+c', hotkey_X)
    keyboard.add_hotkey('space+v', hotkey_Boost)
    keyboard.add_hotkey('space+x', hotkey_Zero)
    keyboard.add_hotkey('space+z', hotkey_changeLeader)
    keyboard.add_hotkey('space+esc', signal.raise_signal, args=(signal.SIGINT,))
    keyboard.wait()