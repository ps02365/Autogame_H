from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
from core_utils.window_capture import WindowCapture
from threading import Thread

die_count = 0
current_slot = 2
last_killed_at = None
running = True
revising = False
auto_die_time_elapsed = time()
wincap = WindowCapture('DreamACE')
move_function_name = 'position_air_plane'
def start_game():
    gw.getWindowsWithTitle('DreamACE')[0].activate()
    sleep(1)
    
    start_auto()

def Training_area():
    global running
    while True:
        if revising == False:
            # Training_area_1 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(1040,575,1220,745)) #s3
            # Training_area_2 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(1040,237,1215,486)) #s9,s6
            # Training_area_3 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(820,370, 1040,594)) #s4,s5
            Training_area_1 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(700,280,870,380)) #s7
            Training_area_2 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(960,300,1040,370)) #s8
            Training_area_3 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(1060,550, 1175,625)) #s6
            Training_area_4 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(690,600, 1020,800)) #s1,2
            if not Training_area_1 or Training_area_2 or Training_area_3 or Training_area_4:
                running = False
                while not Training_area_1 or Training_area_2 or Training_area_3 or Training_area_4:
                    auto_die()
                    Training_area_1 or Training_area_2 or Training_area_3 or Training_area_4
                running = True
            sleep (300)   

def Not_Training_area():
    global running
    while True:
        if revising == False:
            Not_Training_area_1 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(850,295,1220,460)) #s8,s9
            Not_Training_area_2 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(735,382,800,590)) #s4
            Not_Training_area_3 = pyautogui.locateOnScreen('Air_Plane.png', confidence=0.9,region=(994,435, 1190,753)) #s3,s6
            if Not_Training_area_1 or Not_Training_area_2 or Not_Training_area_3:
                running = False
                while Not_Training_area_1 or Not_Training_area_2 or Not_Training_area_3:
                    auto_die()
                    not Not_Training_area_1 or Not_Training_area_2 or Not_Training_area_3
                running = True
            sleep (300)   

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
    auto_skill_process = Thread(target=auto_skill, daemon=True)
    auto_skill_process.start()

    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()

    auto_high_down_process = Thread(target=auto_high_down, daemon=True)
    auto_high_down_process.start()

    auto_high_down_process = Thread(target=auto_high_up, daemon=True)
    auto_high_down_process.start()

    auto_high_down_process = Thread(target=Training_area, daemon=True)
    auto_high_down_process.start()

    auto_high_down_process = Thread(target=Not_Training_area, daemon=True)
    auto_high_down_process.start()

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
        sleep(0.2)

def recharge_fuel(should_start_auto = True):
    skill_socket = pyautogui.locateOnScreen('skill_socket.png', confidence=0.95)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("9")
        sleep(1)
        pydirectinput.press("9")
        sleep(1)

def auto_high_down():
    tick = 10
    height = 300
    global running
    while True:
        if revising == False:
            high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.9,region=(1800,height, 1910,330))
            if not high_point:
                running = False
                sleep(3)
                pydirectinput.keyDown("s")
                while not high_point:
                    pyautogui.moveTo(1920, 700)
                    sleep(1)
                    pyautogui.moveTo((1920/8)*5, 540)
                    high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.9,region=(1800,height, 1910,330))
                running = True
        sleep(tick)
         
def auto_high_up():
    pyautogui.moveTo(1920, 300)
    sleep(2)
    pyautogui.moveTo(1920, 300)
    sleep(2)
    pyautogui.moveTo((1920/8)*5, 540)
    sleep(55)       

def auto_ammunition():
    tick = 1
    while True:
        if running:
            use_ammunition_box()
        sleep(0.02)

def auto_skill():
    tick = 0.01
    while True:
        if running:
            use_hyper_moving()
            use_ber()
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

def check_for_revival():
    button7location = pyautogui.locateOnScreen('dialog.png', confidence=0.6)
    global current_slot
    global die_count
    global last_killed_at
    global running
    global revising
    global start_time_fetch_monster
    global max_monster_count
    if button7location:
        running = False
        revising = True
        start_time_fetch_monster = time()
        max_monster_count = 0
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

def use_ammunition_box():
    ammunition = pyautogui.locateOnScreen('out_of_ammunition.png', confidence=0.6)
    if ammunition:
        sleep(0.1)
        pydirectinput.press("8")
        sleep(0.1)

def use_hyper_moving():
    hyper_moving = pyautogui.locateOnScreen('hyper_moving.png', confidence=0.9)
    if hyper_moving:
        sleep(0.1)
        pydirectinput.press("5")
        sleep(0.1)

def use_ber():
    ber = pyautogui.locateOnScreen('ber.png', confidence=0.9)
    if ber:
        sleep(0.1)
        pydirectinput.press("6")
        sleep(0.1)


def fire():
    sleep(0.3)
    pydirectinput.keyDown("e")
    sleep(0.1)

def start_ground_bomb():
    sleep(0.1)
    pydirectinput.press("3")
    sleep(0.1)

def speed_down_air_plane():
    sleep(0.1)
    pydirectinput.keyDown("s")
    sleep(0.05)
    pydirectinput.keyDown("a")
    sleep(0.1)

def high_down_air_plane():
    sleep(0.1)
    pyautogui.moveTo(1919, 580)
    sleep(0.5)

def position_air_plane():
    right_move = 1920
    pyautogui.moveTo((right_move/8)*5, 540)
    sleep(0.1)

def move_to_ward():
    pyautogui.moveTo(960, 540)

def run_air_plane():
    sleep(0.1)
    pydirectinput.press('w')
    sleep(0.1)

start_game()
