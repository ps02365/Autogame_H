from time import sleep
import pydirectinput
import pyautogui
import keyboard
import win32gui
from plyer import notification

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False

change_form_enable = False

def trigger_change_form_status():
    global change_form_enable
    change_form_enable = not change_form_enable
    if not change_form_enable:
        title = ""
        message = "Không cho phép đổi đội hình"
        notification.notify(title=title,message=message,timeout=1)
        return
    title = ""
    message = "Cho phép đổi đội hình"
    notification.notify(title=title,message=message,timeout=1)                

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

# def ChangeLeaderSlot1():
#     pyautogui.click(button='left',x=1024,y=516) #Choose leader
#     pyautogui.click(button='left',x=1175,y=691) #Authorize
#     pyautogui.click(button='left',x=939,y=554) #Accpept
#     keyupR()
#     pyautogui.press('esc') #Exit F7

# def ChangeLeaderSlot2():
#     pyautogui.click(button='left',x=1024,y=533) #Choose leader
#     pyautogui.click(button='left',x=1175,y=691) #Authorize
#     pyautogui.click(button='left',x=939,y=554) #Accpept
#     keyupR()
#     pyautogui.press('esc') #Exit F7

# def ChangeLeaderSlot3():
#     pyautogui.click(button='left',x=1024,y=550) #Choose leader
#     pyautogui.click(button='left',x=1175,y=691) #Authorize
#     pyautogui.click(button='left',x=939,y=554) #Accpept
#     keyupR()
#     pyautogui.press('esc') #Exit F7

# def ChangeLeaderSlot4():
#     pyautogui.click(button='left',x=1024,y=566) #Choose leader
#     pyautogui.click(button='left',x=1175,y=691) #Authorize
#     pyautogui.click(button='left',x=939,y=554) #Accpept
#     keyupR()
#     pyautogui.press('esc') #Exit F7

# def ChangeLeaderSlot5():
#     pyautogui.click(button='left',x=1024,y=582) #Choose leader
#     pyautogui.click(button='left',x=1175,y=691) #Authorize
#     pyautogui.click(button='left',x=939,y=554) #Accpept
#     keyupR()
#     pyautogui.press('esc') #Exit F7

# def ChangeLeaderSlot6():
#     pyautogui.click(button='left',x=1024,y=597) #Choose leader
#     pyautogui.click(button='left',x=1175,y=691) #Authorize
#     pyautogui.click(button='left',x=939,y=554) #Accpept
#     keyupR()
#     pyautogui.press('esc') #Exit F7

def keydownR():
    # sleep(0.05)
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

# def hotkey_change_leader_slot1():
#     keydownR()
#     ChangeLeaderSlot1()

# def hotkey_change_leader_slot2():
#     keydownR()
#     ChangeLeaderSlot2()

# def hotkey_change_leader_slot3():
#     keydownR()
#     ChangeLeaderSlot3()

# def hotkey_change_leader_slot4():
#     keydownR()
#     ChangeLeaderSlot4()

# def hotkey_change_leader_slot5():
#     keydownR()
#     ChangeLeaderSlot5()

# def hotkey_change_leader_slot6():
#     keydownR()
#     ChangeLeaderSlot6()


if __name__ == "__main__":
    hwd = win32gui.FindWindow(None, "DreamACE")
    if not hwd:
        exit()
    win32gui.SetForegroundWindow(hwd)
    title = "Hướng dẫn đổi đội hình"
    message = "Space + Ctrl để kích hoạt\n    Space + C = Chia damage\n    Space + v = Tăng tốc\n    Space + x = 0ms"
    notification.notify(title=title,message=message,timeout=1)
    keyboard.add_hotkey('ctrl+space',trigger_change_form_status)    
    keyboard.add_hotkey('space+c', hotkey_X)
    keyboard.add_hotkey('space+v', hotkey_Boost)
    keyboard.add_hotkey('space+x', hotkey_Zero)
    keyboard.add_hotkey('space+z', hotkey_changeLeader)
    # keyboard.add_hotkey('num 1', hotkey_change_leader_slot1)
    # keyboard.add_hotkey('num 2', hotkey_change_leader_slot2)
    # keyboard.add_hotkey('num 3', hotkey_change_leader_slot3)
    # keyboard.add_hotkey('num 4', hotkey_change_leader_slot4)
    # keyboard.add_hotkey('num 5', hotkey_change_leader_slot5)
    # keyboard.add_hotkey('num 6', hotkey_change_leader_slot6)
    keyboard.wait()