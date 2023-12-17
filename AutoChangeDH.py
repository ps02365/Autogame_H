from time import sleep
import pydirectinput
import pyautogui
import keyboard

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
    pyautogui.click(button='left',x=1024,y=516) #Choose leader
    pyautogui.click(button='left',x=1175,y=691) #Authorize
    pyautogui.click(button='left',x=939,y=554) #Accpept
    keyupR()
    pyautogui.press('esc') #Exit F7

def ChangeLeaderSlot2():
    pyautogui.click(button='left',x=1024,y=533) #Choose leader
    pyautogui.click(button='left',x=1175,y=691) #Authorize
    pyautogui.click(button='left',x=939,y=554) #Accpept
    keyupR()
    pyautogui.press('esc') #Exit F7

def ChangeLeaderSlot3():
    pyautogui.click(button='left',x=1024,y=550) #Choose leader
    pyautogui.click(button='left',x=1175,y=691) #Authorize
    pyautogui.click(button='left',x=939,y=554) #Accpept
    keyupR()
    pyautogui.press('esc') #Exit F7

def ChangeLeaderSlot4():
    pyautogui.click(button='left',x=1024,y=566) #Choose leader
    pyautogui.click(button='left',x=1175,y=691) #Authorize
    pyautogui.click(button='left',x=939,y=554) #Accpept
    keyupR()
    pyautogui.press('esc') #Exit F7

def ChangeLeaderSlot5():
    pyautogui.click(button='left',x=1024,y=582) #Choose leader
    pyautogui.click(button='left',x=1175,y=691) #Authorize
    pyautogui.click(button='left',x=939,y=554) #Accpept
    keyupR()
    pyautogui.press('esc') #Exit F7

def ChangeLeaderSlot6():
    pyautogui.click(button='left',x=1024,y=597) #Choose leader
    pyautogui.click(button='left',x=1175,y=691) #Authorize
    pyautogui.click(button='left',x=939,y=554) #Accpept
    keyupR()
    pyautogui.press('esc') #Exit F7

def keydownR():
    # sleep(0.05)
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
keyboard.add_hotkey('num 1', hotkey_change_leader_slot1)
keyboard.add_hotkey('num 2', hotkey_change_leader_slot2)
keyboard.add_hotkey('num 3', hotkey_change_leader_slot3)
keyboard.add_hotkey('num 4', hotkey_change_leader_slot4)
keyboard.add_hotkey('num 5', hotkey_change_leader_slot5)
keyboard.add_hotkey('num 6', hotkey_change_leader_slot6)
keyboard.wait()

