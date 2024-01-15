from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
import random
from datetime import datetime
from threading import Thread
import cv2
import numpy as np

die_count = 0
current_slot = 2
last_killed_at = None
running = True
revising = False
start_die_time = time()
def start_game():
    gw.getWindowsWithTitle('DreamACE')[0].activate()
    sleep(1)
    
    start_auto()
    # go_to_s6()
    

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
    # auto_skill_process = Thread(target=auto_skill, daemon=True)
    # auto_skill_process.start()

    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()

    auto_high_down_process = Thread(target=auto_high_down, daemon=True)
    auto_high_down_process.start()


    run_air_plane()
    position_air_plane()
    speed_down_air_plane()
    fire()
    for i in range(100000000):
        check_for_revival()
        if running:
            position_air_plane(i)
            if i % 2 == 0:
                release_fire()
                release_down_air_plane()
            position_air_plane(i)
            # if time() - start_die_time > 600:
            #     auto_die()
            # position_air_plane(i)
        sleep(0.2)

def recharge_fuel(should_start_auto = True):
    skill_socket = locateOnScreen('skill_socket.png', confidence=0.99)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("9")
        sleep(1)
        pydirectinput.press("9")
        sleep(1)

def auto_high_down():
    tick = 10
    global running
    while True:
        if revising == False:
            high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.5,region=(1860,250, 1903,313))
            if not high_point:
                running = False
                sleep(3)
                pydirectinput.keyDown("s")
                while not high_point:
                    pyautogui.moveTo(1920, 700)
                    sleep(1)
                    pyautogui.moveTo(1920, 540)
                    high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.5,region=(1860,250, 1903,313))
                running = True
        sleep(tick)
            

def auto_ammunition():
    tick = 1
    while True:
        if running:
            use_ammunition_box()
        sleep(0.02)

def auto_skill():
    tick = 0.01
    region_fetch_socket = (245, 0, 580, 24)
    while True:
        if running:
            use_hyper_moving()
            use_ber()
            skill_socket = pyautogui.locateOnScreen('skill_socket.png', confidence=0.999, region=region_fetch_socket)
            if skill_socket == None:
                sleep(0.1)
                pydirectinput.press("9")
                sleep(1)
            kit_socket = pyautogui.locateOnScreen('kit_socket.png', confidence=0.999, region=region_fetch_socket)
            if kit_socket == None:
                sleep(0.1)
                pydirectinput.press("0")
                sleep(1)
            # recharge_fuel()d:\pyinstxtractor\auto_enchant_17.exe_extracted\auto_enchant_17.pyc
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
    if button7location:
        running = False
        revising = True
        current_time = datetime.now()
        die_count += 1
        sleep(0.1)
        pydirectinput.press("a")
        sleep(0.1)
        pydirectinput.press("e")
        sleep(0.1)
        pydirectinput.press("s")
        sleep(0.1)

        slots = [
            # 'go_to_s4',
            'go_to_s2',
            # 'go_to_s9',
            # 'go_to_s5'
        ]

        slot_to_go = random.choice(slots)
        # if last_killed_at is None or (current_time - last_killed_at).total_seconds() > 600:
        #     slot_to_go = random.choice(slots)
        # else:
        #     slot_to_go = 'go_to_s3'
            
        last_killed_at = current_time
        pydirectinput.press('esc')
        sleep(1)

        
        eval(f"{slot_to_go}()")
        pydirectinput.keyDown("s")
        revising = False
        running = True

def go_to_s4():
    sleep(1.5)
    pyautogui.moveTo(955, 547)
    sleep(0.1)
    pydirectinput.press('w')
    sleep(5)
    pyautogui.moveTo(0, 540)
    sleep(0.5)
    pyautogui.moveTo(960, 540)
    sleep(5)
    pyautogui.moveTo(960, 540)
    sleep(10)

def go_to_s2():
    sleep(1.5)
    pyautogui.moveTo(955, 550)
    sleep(0.1)
    pydirectinput.press('w')
    sleep(5)
    pyautogui.moveTo(0, 540)
    sleep(0.5)
    pyautogui.moveTo(960, 540)
    sleep(5)
    pyautogui.moveTo(960, 540)
    sleep(6)

def go_to_s3():
    sleep(1.5)
    pyautogui.moveTo(920, 630)
    sleep(0.1)
    pydirectinput.press('w')
    sleep(1.5)
    pyautogui.moveTo(970, 570)
    sleep(0.5)

def go_to_s5():
    sleep(1.5)
    pydirectinput.press('w')
    sleep(0.1)
    pydirectinput.press('w')
    pyautogui.moveTo(960, 560)
    sleep(14)


def go_to_s6():
    sleep(1.5)
    pyautogui.moveTo(960, 560)
    sleep(0.1)
    pydirectinput.press('w')
    sleep(1)
    pyautogui.moveTo(1920, 540)
    sleep(0.65)
    pyautogui.moveTo(960, 540)
    sleep(8)
    pyautogui.moveTo(480, 540)
    pydirectinput.keyDown('r')
    sleep(0.5)
    pydirectinput.keyUp('r')
    sleep(2)
    pyautogui.moveTo(960, 540)
    sleep(2)

def go_to_s9():
    height_go_up = 490
    height_blance = 540
    height_go_down = 600
    sleep(1.5)
    pyautogui.moveTo(960, height_go_up)
    sleep(0.1)
    pydirectinput.press('w')
    sleep(1)
    pydirectinput.keyDown('a')
    pyautogui.moveTo(1920, height_go_up)
    sleep(0.25)
    pydirectinput.keyUp('a')
    pyautogui.moveTo(960, height_blance)
    sleep(13)
    pyautogui.moveTo(960, height_go_down)
    sleep(8.5)
    


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
    ammunition = locateOnScreen('out_of_ammunition.png', confidence=0.4)
    if ammunition:
        sleep(0.1)
        pydirectinput.press("8")
        sleep(0.1)

def use_hyper_moving():
    hyper_moving = pyautogui.locateOnScreen('hyper_moving.png', confidence=0.9)
    if hyper_moving:
        sleep(0.1)
        pydirectinput.press("1")
        sleep(0.1)

def use_ber():
    ber = pyautogui.locateOnScreen('ber.png', confidence=0.9)
    if ber:
        sleep(0.1)
        pydirectinput.press("2")
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

def position_air_plane(i = -1):
    stop_to_shoot_x = 1060
    right_move = 1600
    stop_to_shoot_second = 0.05
    # if i > 0 and i % 40 == 0:
    #     high_down_air_plane()
    # pyautogui.moveTo(right_move, 540)
    # sleep(0.1)
    # pyautogui.moveTo(stop_to_shoot_x, 540)
    # sleep(stop_to_shoot_second)
    pyautogui.moveTo(right_move, 540)
    sleep(0.1)
    # pyautogui.moveTo(stop_to_shoot_x, 540)
    # sleep(stop_to_shoot_second)
    # pyautogui.moveTo(right_move, 540)
    # sleep(0.1)

def locateOnScreen(template_path, region = None, confidence = 0.9):
    # Load the screen image
    if region:
        screen_image = pyautogui.screenshot(region=(9, 4, 29-9, 29-4))
    else:
        screen_image = pyautogui.screenshot()

    screen_image = np.array(screen_image)
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_RGB2BGR)

    # Load the template image
    template = cv2.imread(template_path)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)

    # Match the template in the screen image
    result = cv2.matchTemplate(screen_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Define a threshold to determine if the template is found
    threshold = confidence  # You can adjust this value as needed
    if max_val >= threshold:
        # Template found
        w, h = template.shape[:-1]
        return (min_loc[0], min_loc[1], w, h)
    else:
        return None

def run_air_plane():
    sleep(0.1)
    pydirectinput.press('w')
    sleep(0.1)

start_game()
