from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
import cv2
import numpy as np
from threading import Thread
import win32gui
from core_utils import auto_helper
from datetime import datetime
import random

pyautogui.FAILSAFE = False

start_time_switch_skill = time()
start_time_fetch_monster = time()
max_monster_count = 0
running = True
current_skill = None
last_killed_at = None
revising = False

MULTI_TARGET_SKILL = {
    "name": "multi_target",
    "img": "multi_target.png",
    "press": "7",
    "time_to_swtich": 3
}

GB_SKILL = {
    "name": "gb",
    "img": "GB.png",
    "press": "3",
    "time_to_swtich": 30
}

def start_game():
    hwnd = win32gui.FindWindow(None, "DreamACE")
    if not hwnd:
        raise Exception("Not found DreamACE window")
    win32gui.SetForegroundWindow(hwnd)
    sleep(1)
    start_auto()


def start_auto():
    global start_time_fetch_monster
    global max_monster_count
    global current_skill

    current_skill = MULTI_TARGET_SKILL

    auto_switch_skill_bg_process = Thread(target=auto_switch_skill_bg, daemon=True)
    auto_switch_skill_bg_process.start()

    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()

    auto_high_down_process = Thread(target=auto_high_down, daemon=True)
    auto_high_down_process.start()

    auto_refuel_process = Thread(target=auto_refuel, daemon=True)
    auto_refuel_process.start()

    # auto_detect_monster_process = Thread(target=auto_helper.auto_detect_monster, daemon=True)
    # auto_detect_monster_process.start()
    
    run_air_plane()
    position_air_plane()
    speed_down_air_plane()
    fire()
    
    i = 0
    while True:
        if running:
            position_air_plane()
            if i % 4 == 0 and i >= 1:
                release_fire()
                release_down_air_plane()
            if time() - start_time_fetch_monster > 120:
                if max_monster_count < 7:
                    auto_die()
                start_time_fetch_monster = time()
                max_monster_count = 0
            if i % 5 == 0 and i >= 1:
                check_for_revival()
        i += 1
        sleep(0.2)

def auto_high_down():
    tick = 20
    yaxis = 270
    width = 40
    height = 60
    conf = 0.6
    global running
    while True:
        if revising == False:
            high_point = pyautogui.locateOnScreen('current_height.png', confidence=conf,region=(1880,yaxis, width,height))
            if not high_point:
                # running = False
                pydirectinput.keyDown("s")
                time_to_high_down = time()
                while not high_point and time() - time_to_high_down < 30:
                    pyautogui.moveTo(960, 1080)
                    sleep(1.5)
                    pyautogui.moveTo(960, 400)
                    sleep(1)
                    pyautogui.moveTo(960, 1080)
                    sleep(1.5)
                    high_point = pyautogui.locateOnScreen('current_height.png', confidence=conf,region=(1880,yaxis, width,height))
                    time_to_high_down =  time()
                # running = True
        sleep(tick)

def auto_up_and_down_shooting():
    tick = 0.01
    while True:
        if running:
            if current_skill["name"] == "multi_target":
                pyautogui.moveTo(1920,200, 0.7)
                pyautogui.moveTo(1920,850, 1.2)
        sleep(tick)

def auto_refuel():
    tick = 60
    while True:
        if running:
            recharge_fuel()
        sleep(tick)

def auto_ammunition():
    tick = 1
    while True:
        if running:
            use_ammunition_box()
        sleep(0.05)

def auto_switch_skill_bg():
    tick = 0.1
    global start_time_switch_skill
    global current_skill
    while True:
        if running:
            correct_skill()
            if time() - start_time_switch_skill > current_skill["time_to_swtich"]:
                print("Time to switch: {}----------".format(current_skill["time_to_swtich"]))
                switch_skill()
                start_time_switch_skill = time()

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
        sleep(tick)
            

def correct_skill():
    if current_skill["name"] == "multi_target":
        gbImage = pyautogui.locateOnScreen('GB.png', region=(245, 0, 580, 300),confidence=0.7)
        while gbImage:
            pydirectinput.press("3")
            sleep(0.1)
            gbImage = pyautogui.locateOnScreen('GB.png', region=(245, 0, 580, 300),confidence=0.7)
    elif current_skill["name"] == "gb":
        multi_target_image = pyautogui.locateOnScreen('multi_target.png', region=(245, 0, 580, 300),confidence=0.7)    
        while multi_target_image:
            pydirectinput.press("7")
            sleep(0.1)
            multi_target_image = pyautogui.locateOnScreen('multi_target.png', region=(245, 0, 580, 300),confidence=0.7)    
        
    skillImg = pyautogui.locateOnScreen(current_skill["img"], region=(245, 0, 580, 24),confidence=0.7)
    if skillImg is None:
        sleep(0.1)
        pydirectinput.press(current_skill["press"])
        sleep(0.1)

def switch_skill():
    gbImage = pyautogui.locateOnScreen('GB.png', region=(245, 0, 580, 300),confidence=0.7)
    multi_target_image = pyautogui.locateOnScreen('multi_target.png', region=(245, 0, 580, 300),confidence=0.7)
    global current_skill
    print("------switch_skill-------")
    print(f"current skill: {current_skill}")
    if gbImage:
        sleep(0.1)
        pydirectinput.press("3")
        sleep(0.1)
        pydirectinput.press("7")
        current_skill = MULTI_TARGET_SKILL
    elif multi_target_image:
        sleep(0.1)
        pydirectinput.press("7")
        sleep(0.1)
        pydirectinput.press("3")
        current_skill = GB_SKILL

def recharge_fuel(should_start_auto = True):
    skill_socket = pyautogui.locateOnScreen('skill_socket.png', region=(245, 0, 580, 24), confidence=0.95)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("9")
        sleep(1)
        pydirectinput.press("9")
        sleep(1)

def auto_die():
    global running
    running = False
    sleep(4)
    pydirectinput.press("a")
    sleep(0.1)
    pydirectinput.press("e")
    sleep(0.1)
    skill_socket = pyautogui.locateOnScreen('kit_socket.png',  region=(245, 0, 580, 50), confidence=0.9)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("0")
        sleep(1)
    pyautogui.moveTo(960, 1080)
    revise_dialog = pyautogui.locateOnScreen('dialog.png', confidence=0.55)
    pydirectinput.keyDown('space')
    while not revise_dialog:
        sleep(0.5)
        pyautogui.moveTo(960, 1080)
        revise_dialog = pyautogui.locateOnScreen('dialog.png', confidence=0.55)
    pydirectinput.keyUp('space')
    check_for_revival()

def check_for_revival():
    global running
    global start_time_fetch_monster
    global start_time_switch_skill
    global max_monster_count
    global current_skill
    global last_killed_at
    global revising
    button7location = pyautogui.locateOnScreen('dialog.png', confidence=0.55)
    if button7location:
        revising = True
        running = False
        start_time_fetch_monster = time()
        max_monster_count = 0
        current_time = datetime.now()
        pydirectinput.press("a")
        sleep(0.1)
        pydirectinput.press("e")
        sleep(0.1)
        pydirectinput.press("s")
        sleep(0.1)
        pydirectinput.press('esc')
        slots = [
            # 'go_to_s4',
            'go_to_s2',
            'go_to_s9',
            # 'go_to_s5'
        ]

        if last_killed_at is None or (current_time - last_killed_at).total_seconds() > 600:
            slot_to_go = random.choice(slots)
        else:
            slot_to_go = 'go_to_s3'
            
        last_killed_at = current_time
        pydirectinput.press('esc')
        sleep(1)

        
        eval(f"{slot_to_go}()")
        
        current_skill = MULTI_TARGET_SKILL
        start_time_switch_skill = time()
        sleep(0.1)
        pydirectinput.keyDown("s")
        sleep(0.1)
        pydirectinput.keyDown("e")
        running = True
        revising = False

def release_down_air_plane():
    speed_down_air_plane()

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

def release_fire():
    sleep(0.1)
    pydirectinput.keyUp("e")
    sleep(0.1)
    pydirectinput.keyDown("e")
    sleep(0.1)

def use_ammunition_box():
    ammunition = pyautogui.locateOnScreen('out_of_ammunition.png', confidence=0.58)
    if ammunition:
        sleep(0.1)
        pydirectinput.press("8")
        sleep(0.1)

def fire():
    sleep(0.3)
    pydirectinput.press("e", 3)
    sleep(0.1)
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

def position_air_plane():
    sleep(0.1)
    pyautogui.moveTo(1919, 540)
    sleep(0.1)

def run_air_plane():
    sleep(0.1)
    pydirectinput.press('w')
    sleep(0.1)
    pydirectinput.keyDown('s')
    sleep(0.1)

start_game()