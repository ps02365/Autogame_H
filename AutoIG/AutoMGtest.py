from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
# from core_utils.window_capture import WindowCapture
from threading import Thread
import win32gui

die_count = 0
current_slot = 2
last_killed_at = None
running = True
revising = False
# wincap = WindowCapture('DreamACE')
move_function_name = 'position_air_plane'

def start_game():
    # hwnd = win32gui.FindWindow(None, "DreamACE")
    # if not hwnd:
    #     raise Exception("Not found DreamACE window")
    # win32gui.SetForegroundWindow(hwnd)
    # sleep(1)
    
    start_auto()

def check_for_revival():
    button7location = pyautogui.locateOnScreen('dialog.png', confidence=0.6)
    global current_slot
    global die_count
    global last_killed_at
    global running
    global revising
    if button7location:
        running = False
        revising = True
        die_count += 1
        sleep(0.1)
        pydirectinput.press("a")
        sleep(0.1)
        pydirectinput.press("e")
        sleep(0.1)
        pydirectinput.press("s")
        sleep(0.1)
        pydirectinput.press('esc')
        sleep(1)
        pydirectinput.keyDown("s")
        revising = False
        running = True      

def Training_area():
    global running
    while True:
        if revising == False:
            Training_area_1 = pyautogui.locateOnScreen('1920x1080/Air_Plane.png', confidence=0.9,region=(820,345,1060,440))
            Training_area_2 = pyautogui.locateOnScreen('1920x1080/Air_Plane.png', confidence=0.9,region=(1860,0, 1903,275))
            Training_area_3 = pyautogui.locateOnScreen('1920x1080/Air_Plane.png', confidence=0.9,region=(1860,0, 1903,275))
            if not Training_area_1:
                running = False
                while not Training_area_1:
                    auto_die()
                    Training_area_1 
            sleep (3)

def auto_die():
    global running
    global last_killed_at
    running = False
    last_killed_at = None
    sleep(4)
    skill_socket = pyautogui.locateOnScreen('kit_socket.png', confidence=0.95)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("0")
        sleep(1)
    sleep(0.1)
    pydirectinput.press("a")
    sleep(0.1)
    pydirectinput.press("e")
    sleep(0.1)
    pyautogui.moveTo(960, 1080)
    revise_dialog = pyautogui.locateOnScreen('dialog.png', confidence=0.6)
    pydirectinput.keyDown('space')
    while not revise_dialog:
        sleep(0.5)
        pyautogui.moveTo(960, 1080)
        revise_dialog = pyautogui.locateOnScreen('dialog.png', confidence=0.6)
    pydirectinput.keyUp('space')
    check_for_revival()



def start_auto():
    for i in range(100000000):
        if i % 2 == 0:
            Training_area()


if __name__ == "__main__":
    start_game()
