from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
from core_utils.window_capture import WindowCapture
from threading import Thread
import win32gui

die_count = 0
current_slot = 2
last_killed_at = None
running = True
revising = False
wincap = WindowCapture('DreamACE')
move_function_name = 'position_air_plane'

def start_game():
    hwnd = win32gui.FindWindow(None, "DreamACE")
    if not hwnd:
        raise Exception("Not found DreamACE window")
    win32gui.SetForegroundWindow(hwnd)
    sleep(1)
    
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

def auto_high_down():
    tick = 10
    height = 270
    global running
    while True:
        if revising == False:
            high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.9,region=(1860,height, 1903,313))
            if not high_point:
                running = False
                sleep(3)
                pydirectinput.keyDown("s")
                while not high_point:
                    pyautogui.moveTo(1920, 700)
                    sleep(1)
                    pyautogui.moveTo(1920, 540)
                    high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.9,region=(1860,height, 1903,313))
                running = True
        sleep(tick)         

def auto_ammunition():
    tick = 1
    while True:
        if running:
            use_ammunition_box()
        sleep(0.02)

def use_ammunition_box():
    ammunition = pyautogui.locateOnScreen('out_of_ammunition.png', confidence=0.6)
    if ammunition:
        sleep(0.1)
        pydirectinput.press("8")
        sleep(0.1)

def auto_skill():
    tick = 0.01
    while True:
        if running:
            skill_socket = pyautogui.locateOnScreen('skill_socket.png', confidence=0.95)
            if skill_socket == None:
                sleep(0.1)
                pydirectinput.press("9")
                sleep(1)
            skill_socket = pyautogui.locateOnScreen('kit_socket.png', confidence=0.95)
            if skill_socket == None:
                sleep(0.1)
                pydirectinput.press("0")
                sleep(1)
            recharge_fuel()
        sleep(tick)

def auto_refuel():
    tick = 60
    while True:
        if running:
            recharge_fuel()
        sleep(tick)

def recharge_fuel(should_start_auto = True):
    skill_socket = pyautogui.locateOnScreen('skill_socket.png', confidence=0.95)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("9")
        sleep(1)
        pydirectinput.press("9")
        sleep(1)

def release_down_air_plane():
    sleep(0.1)
    pydirectinput.keyUp("a")
    sleep(0.1)
    speed_down_air_plane()

def release_fire():
    sleep(0.1)
    pydirectinput.keyUp("e")
    sleep(0.1)
    pydirectinput.keyDown("e")
    sleep(0.1)

def fire():
    sleep(0.3)
    pydirectinput.keyDown("e")
    sleep(0.1)

def speed_down_air_plane():
    sleep(0.1)
    pydirectinput.keyDown("s")
    sleep(0.05)
    pydirectinput.keyDown("a")
    sleep(0.1)

def position_air_plane():
    pyautogui.moveTo((1920/8)*5, 540)
    sleep(0.1)

def run_air_plane():
    sleep(0.1)
    pydirectinput.press('c')
    sleep(0.1)

def auto_die():
    while True:
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
        sleep(600)
    

def start_auto():
    auto_skill_process = Thread(target=auto_skill, daemon=True)
    auto_skill_process.start()

    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()

    auto_high_down_process = Thread(target=auto_high_down, daemon=True)
    auto_high_down_process.start()

    auto_die_process = Thread(target=auto_die,daemon=True)
    auto_die_process.start()
    
    run_air_plane()
    position_air_plane()
    speed_down_air_plane()
    fire()
    for i in range(100000000):
        check_for_revival()
        if running:
            eval("{}()".format(move_function_name))
            if i % 2 == 0:
                release_fire()
                release_down_air_plane()
            eval("{}()".format(move_function_name))
        sleep(0.2)

if __name__ == "__main__":
    start_game()
