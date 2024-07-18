from time import sleep
import pyautogui
import keyboard
import win32gui
import pydirectinput
import sys
import signal
from threading import Thread
import configparser

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

def read_config_from_ini(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config
config = read_config_from_ini('config.ini')

roll_1 = config['ROLL']['Trigger']
roll_2 = config['ROLL']['PVE']
roll_3 = config['ROLL']['Accuracy']
roll_4 = config['ROLL']['Pierce']    
roll_5 = config['ROLL']['DMG']

flightform_1 = config['FLIGHTFORM']['Trigger']
flightform_2 = config['FLIGHTFORM']['Xform']
flightform_3 = config['FLIGHTFORM']['Boostform']
flightform_4 = config['FLIGHTFORM']['Zeroform']
flightform_5 = config['FLIGHTFORM']['Changeleader']

def trigger_change_roll_status():
    global roll_enable
    roll_enable = not roll_enable
    if not roll_enable:
        print('\nKhông cho phép roll')
        sleep(0.1)
        pydirectinput.keyDown('r')
        sleep(0.1)
        pydirectinput.keyUp('r')
        sleep(0.1)
        return
    pydirectinput.keyDown('r')
    sleep(0.1)
    pydirectinput.keyUp('r')
    sleep(0.1)
    pydirectinput.keyDown('r')
    sleep(0.1)
    pydirectinput.keyUp('r')
    sleep(0.1)
    print('\nCho phép roll')           

def trigger_change_form_status():
    global change_form_enable
    change_form_enable = not change_form_enable
    if not change_form_enable:
        pydirectinput.keyDown('esc')
        sleep(0.1)
        pydirectinput.keyUp('esc')
        sleep(0.1)
        pydirectinput.keyDown('r')
        sleep(0.1)
        pydirectinput.keyUp('r')
        sleep(0.1)
        print('\nKhông cho phép đổi đội hình')
        return
    pydirectinput.keyDown('esc')
    sleep(0.1)
    pydirectinput.keyUp('esc')
    sleep(0.1)
    pydirectinput.keyDown('r')
    sleep(0.1)
    pydirectinput.keyUp('r')
    sleep(0.1)
    pydirectinput.keyDown('r')
    sleep(0.1)
    pydirectinput.keyUp('r')
    sleep(0.1)
    print('\nCho phép đổi đội hình')                   

def signal_handler(sig, frame):
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)

def auto_ammunition():
    if not roll_enable:
        return    
    while True:
        if running:
            use_ammunition_box()
        sleep(0.5)

def use_ammunition_box():
    left = 0    
    top = 0
    width = 320
    height = 50
    region_to_fetch = (left,top,width,height)   
    try:
        ammunition = pyautogui.locateOnScreen('./1920x1080/out_of_ammunition.png', region = region_to_fetch, confidence=0.9, grayscale= False)
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
        Not_Found_Tick()
        return locate_image_tick()
    
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
    except pyautogui.ImageNotFoundException as e:
        print("Arrange image not found:", e)
        return 

def Not_Found_Tick():
    tick = 0.01
    pydirectinput.keyDown("esc")    
    sleep(tick)
    pydirectinput.keyUp("esc")  
    sleep(tick)
    pydirectinput.keyDown("b")    
    sleep(tick)
    pydirectinput.keyUp("b")
    sleep(tick) 

def Stop():
    tick = 0.01
    pydirectinput.keyDown('b')
    # sleep(tick)
    pydirectinput.keyUp('b')
    # sleep(tick)
    image_position_tick = locate_image_tick()
    if image_position_tick:
        left, top, width, height = image_position_tick
    pyautogui.click(left+15,top+20) 
    # sleep(tick)
    pydirectinput.keyDown("i")    
    # sleep(tick)
    pydirectinput.keyUp("i")  

#Trái sang phải, trên xuống dưới

def slot_1(left_1, top_1):
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        left, top, width, height = image_position_inventory
        left_1 = left
        top_1 = top
    else:
        print("Unable to locate arrange image.")

    return left_1, top_1

left_1,top_1 = slot_1
# left_2,top_2 = slot_2
# left_3,top_3 = slot_3
# left_4,top_4 = slot_4
# left_5,top_5 = slot_5
# left_6,top_6 = slot_6
# left_7,top_7 = slot_7
# left_8,top_8 = slot_8
# left_9,top_9 = slot_9
# left_10,top_10 = slot_10


def Accuracy():
    tick =0
    if not roll_enable:
        return    
    Stop()
    # sleep(0.01)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll CX')
        left, top, width, height = image_position_inventory
    try:    
        pyautogui.doubleClick(left-300,top-225) 
        pyautogui.doubleClick(left-300,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-270,top-225) 
        pyautogui.doubleClick(left-270,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-300,top-200) 
        pyautogui.doubleClick(left-300,top-200)
        sleep(tick)
        pyautogui.doubleClick(left-270,top-200) 
        pyautogui.doubleClick(left-270,top-200)  
        sleep(tick)
        pydirectinput.keyDown('c')
        sleep(tick)
        pydirectinput.keyUp('c')
    except Exception as e:
        print("Error:", e)
        pydirectinput.keyDown("c")    
        sleep(0.1)
        pydirectinput.keyUp("c")


def Pierce():
    tick = 0
    if not roll_enable:
        return   
    Stop()
    sleep(0.01)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll XP')
        left, top, width, height = image_position_inventory 
    try:
        pyautogui.doubleClick(left-200,top-225)
        pyautogui.doubleClick(left-200,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-170,top-225)
        pyautogui.doubleClick(left-170,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-200,top-200)
        pyautogui.doubleClick(left-200,top-200)
        sleep(tick)
        pyautogui.doubleClick(left-170,top-200)
        pyautogui.doubleClick(left-170,top-200) 
        sleep(tick)
        pydirectinput.keyDown('c')
        sleep(tick)
        pydirectinput.keyUp('c')
    except Exception as e:
        print("Error:", e)
        pydirectinput.keyDown("c")    
        sleep(0.1)
        pydirectinput.keyUp("c")

def DMG():
    tick = 0
    if not roll_enable:
        return   
    Stop()
    sleep(0.01)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll DMG')
        left, top, width, height = image_position_inventory 
    try:
        pyautogui.doubleClick(left-200,top-225)
        pyautogui.doubleClick(left-200,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-140,top-225)
        pyautogui.doubleClick(left-140,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-200,top-200)
        pyautogui.doubleClick(left-200,top-200)
        sleep(tick)
        pyautogui.doubleClick(left-140,top-200)
        pyautogui.doubleClick(left-140,top-200) 
        sleep(tick)
        pydirectinput.keyDown('c')
        sleep(tick)
        pydirectinput.keyUp('c')
    except Exception as e:
        print("Error:", e)
        pydirectinput.keyDown("c")    
        sleep(0.1)
        pydirectinput.keyUp("c")

def PVE():
    tick = 0
    if not roll_enable:
        return   
    Stop()
    sleep(0.01)
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        # print("Image found at:", image_position_inventory)
        print('Roll DMG')
        left, top, width, height = image_position_inventory 
    try:
        pyautogui.doubleClick(left-200,top-225) #Giáp
        pyautogui.doubleClick(left-200,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-110,top-225) #Súng
        pyautogui.doubleClick(left-110,top-225)
        sleep(tick)
        pyautogui.doubleClick(left-270,top-200) #Bùa
        pyautogui.doubleClick(left-270,top-200)  
        sleep(tick)
        pyautogui.doubleClick(left-110,top-200) #TL
        pyautogui.doubleClick(left-110,top-200) 
        sleep(tick)
        pydirectinput.keyDown('c')
        sleep(tick)
        pydirectinput.keyUp('c')
    except Exception as e:
        print("Error:", e)
        pydirectinput.keyDown("c")    
        sleep(0.1)
        pydirectinput.keyUp("c")

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

# def Pierce_form():
#     pyautogui.click(button='left',x=201,y=1049) #change chat channel
#     pyautogui.click(button='left',x=320,y=1067) #open F7
#     pyautogui.click(button='left',x=837,y=552) #Choose flight form list
#     pyautogui.click(button='left',x=774,y=631) #Choose flight form "Pierce"  
#     pyautogui.click(button='left',x=980,y=690) #Apply
#     pyautogui.click(button='left',x=16,y=1050) #All chat channel
#     pyautogui.click(button='left',x=960,y=540) #Move to Central
#     keyupR()
#     pyautogui.press('esc') #Exit F7

# def DMG_form():
#     pyautogui.click(button='left',x=201,y=1049) #change chat channel
#     pyautogui.click(button='left',x=320,y=1067) #open F7
#     pyautogui.click(button='left',x=837,y=552) #Choose flight form list
#     pyautogui.click(button='left',x=774,y=631) #Choose flight form "DMG"  
#     pyautogui.click(button='left',x=980,y=690) #Apply
#     pyautogui.click(button='left',x=16,y=1050) #All chat channel
#     pyautogui.click(button='left',x=960,y=540) #Move to Central
#     keyupR()
#     pyautogui.press('esc') #Exit F7

def ChangeLeader():
    pyautogui.click(button='left',x=201,y=1049) #change chat channel
    pyautogui.click(button='left',x=320,y=1067) #open F7
    pyautogui.click(button='left',x=16,y=1050) #All chat channel
    pyautogui.click(button='left',x=960,y=540) #Move to Central
    keyupR()

def keydownR():
    sleep(0.01)
    pydirectinput.keyDown('r')

def keyupR():
    sleep(0.01)
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
    print ("Powered by Hwng Code Lỏd")
    print ("\nVersion: 030524")
    sleep(0.5)
    # print ("\nHướng dẫn đổi đội hình\nSpace + F1 để kích hoạt\n    Space + Z = Giao diện đội hình\n    Space + C = Chia damage\n    Space + V = Tăng tốc\n    Space + X = 0ms\nSpace + F4 để tắt")
    # sleep(0.5)
    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()
    print('\nKích hoạt tự động nạp đạn')
    sleep(0.5)
    print('\nBắt đầu')
    sleep(0.5)
    # hwd = win32gui.FindWindow(None, "DreamACE")
    # if not hwd:
    #     print ('\nKhông tìm thấy game.')
    #     sleep(1)
    #     print ('\nThoát phần mềm trong 2 giây.')
    #     sleep(1)
    #     print('2')
    #     sleep(1)
    #     print('1')
    #     sleep(1)
    #     exit()
    # win32gui.SetForegroundWindow(hwd)
    # pyautogui.moveTo(x=960, y=540)
    keyboard.add_hotkey(roll_1,trigger_change_roll_status)
    keyboard.add_hotkey(roll_2,PVE)
    keyboard.add_hotkey(roll_3,Accuracy)
    keyboard.add_hotkey(roll_4,Pierce)
    keyboard.add_hotkey(roll_5,DMG)
    keyboard.add_hotkey(flightform_1,trigger_change_form_status)   
    keyboard.add_hotkey(flightform_2, hotkey_X)
    keyboard.add_hotkey(flightform_3, hotkey_Boost)
    keyboard.add_hotkey(flightform_4, hotkey_Zero)
    keyboard.add_hotkey(flightform_5, hotkey_changeLeader)
    keyboard.add_hotkey('space+F4', signal.raise_signal, args=(signal.SIGINT,))
    keyboard.wait()
