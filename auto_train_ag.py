import pyautogui
import cv2
import numpy as np
from core_utils.window_capture import WindowCapture
import torch
import os
from time import time,sleep
import pydirectinput
import win32gui
import random

wincap = WindowCapture('DreamACE')
hwnd = win32gui.FindWindow(None, "DreamACE")
max_number_of_monster = 0
monster_killed_in_one_minute = 0
monster_killed = 0
elapsed_time_one_minute = time()
start_time = time()
time_to_move = time()
model = torch.hub.load('.\\yolov7', 'custom', 'best.pt', source='local')
# heal_bar_img = 'hear_bar_fov_60_crop.png'
# heal_bar_plus_x = 42
# heal_bar_plus_y = 20

loss_heal_bar_img = 'heal_loss_crop.png'
heal_bar_img = 'heal_crop.png'
heal_bar_plus_x = 35
heal_bar_plus_y = 35
shooting = False
run_count = 0
start_die_time = time()
min_limit_max_number_of_monster = 4

heal_confidence = 0.8
if not hwnd:
    raise Exception("Not found DreamACE window")
win32gui.SetForegroundWindow(hwnd)

def reset():
    global max_number_of_monster
    global monster_killed
    global start_time
    global time_to_move
    global start_die_time
    global monster_killed_in_one_minute
    global elapsed_time_one_minute
    monster_killed_in_one_minute = 0
    max_number_of_monster = 0
    monster_killed = 0
    start_time = time()
    time_to_move = time()
    start_die_time = time()
    elapsed_time_one_minute = time()

def auto_die():
    pydirectinput.press("space")
    sleep(4)
    skill_socket = pyautogui.locateOnScreen('kit_socket.png',  region=(245, 0, 580, 24), confidence=0.9)
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
    while not revise_dialog:
        sleep(0.5)
        pyautogui.moveTo(960, 1080)
        revise_dialog = pyautogui.locateOnScreen('dialog.png', confidence=0.58)
    revise()

def move_arround_while_firing():
    choice = random.choice(list([1]))
    if choice == 1:
        pydirectinput.keyDown('d')
        sleep(0.2)
        pydirectinput.keyUp('d')
    else:
        move()

def move(sleep_time = 2):
    pydirectinput.keyDown('w')
    sleep(sleep_time)
    pydirectinput.keyUp('w')
    # sleep(0.05)
    # pydirectinput.keyDown('d')
    # sleep(1)
    # pydirectinput.keyUp('d')


def use_ammunition_box():
    ammunition = pyautogui.locateOnScreen('out_of_ammunition.png', confidence=0.6)
    if ammunition:
        sleep(0.1)
        pydirectinput.press("8")
        sleep(0.1)

def revise():
    reset()
    pydirectinput.press('w', 3)
    pyautogui.mouseUp(button="left")
    sleep(0.1)
    pydirectinput.press('esc')
    sleep(0.5)
    pyautogui.moveTo(960, 1080)
    tctd = pyautogui.locateOnScreen('tctd.png', region=(245, 0, 580, 24), confidence=0.7)
    while tctd is None:
        tctd = pyautogui.locateOnScreen('tctd.png', region=(245, 0, 580, 24), confidence=0.7)
        pyautogui.moveTo(960, 1080)
        pydirectinput.press('c')
        pydirectinput.press('1')

def get_monster():
    # Take a screenshot 
    screen = wincap.get_screenshot()
    # screen = pyautogui.screenshot()
    # Convert the output to a numpy array
    # screen_array = np.array(screen)
    # Crop out the region we want - height, width, channels   
    cropped_region = screen
    # Convert the color channel order
    corrected_colors = cv2.cvtColor(cropped_region, cv2.COLOR_RGB2BGR)
    # corrected_colors = cropped_region
    
    # Make detections
    model.conf = 0.33
    results = model(corrected_colors)

    return results
    
def find_heal_bar():
    region = (0, 100, 1920, 980)
    heal_bar = pyautogui.locateOnScreen(heal_bar_img, region=region,confidence=heal_confidence)
    if heal_bar:
        x = heal_bar.left + heal_bar_plus_x
        y = heal_bar.top + heal_bar_plus_y
        pyautogui.moveTo(x, y)
        return (x, y)
    
    loss_heal_bar = pyautogui.locateOnScreen(loss_heal_bar_img, region=region,confidence=heal_confidence)
    if loss_heal_bar:
        x = loss_heal_bar.left - 28
        y = loss_heal_bar.top + heal_bar_plus_y
        pyautogui.moveTo(x, y)
        return (x, y)
    return None

while True:
    run_count += 1
    pyautogui.moveTo(960, 540)
    die = pyautogui.locateOnScreen('dialog.png', region=(670, 450, 580, 180), confidence=0.55)
    if die:
        revise()
    if run_count % 2 == 0:
        use_ammunition_box()
    # if time() - start_time > 60 and (monster_killed < 3 or max_number_of_monster < min_limit_max_number_of_monster):
    #     auto_die()
    if time() - start_die_time > 180:
        if monster_killed < 8:
            auto_die()
        start_die_time = time()
        monster_killed = 0

    results = get_monster()
    data = results.pandas().xyxy[0]
    if len(data) > max_number_of_monster:
        max_number_of_monster = len(results.pandas().xyxy[0])

    if run_count % 5 and len(data) < 3:
        move_arround_while_firing()
        results = get_monster()
        data = results.pandas().xyxy[0]
        while len(data) < 3:
            tctd = pyautogui.locateOnScreen('tctd.png', region=(245, 0, 580, 24), confidence=0.7)
            if tctd:
                pydirectinput.press('1')
            
            die = pyautogui.locateOnScreen('dialog.png', region=(670, 450, 580, 180), confidence=0.55)
            if die:
                break
            results = get_monster()
            data = results.pandas().xyxy[0]
            move_arround_while_firing()
    
    if time() - elapsed_time_one_minute > 60:
        print("Monster kill in one minute: {}".format(monster_killed_in_one_minute))
        if monster_killed_in_one_minute < 5:
            move_arround_while_firing()
            results = get_monster()
            data = results.pandas().xyxy[0]
            filter_on_center_screen = data.query('xmin > 300 & xmin < 1820')
            while len(filter_on_center_screen) < 3:
                tctd = pyautogui.locateOnScreen('tctd.png', region=(245, 0, 580, 24), confidence=0.7)
                if tctd:
                    pydirectinput.press('1')
                
                die = pyautogui.locateOnScreen('dialog.png', region=(670, 450, 580, 180), confidence=0.55)
                if die:
                    break
                results = get_monster()
                data = results.pandas().xyxy[0]
                filter_on_center_screen = data.query('xmin > 300 & xmin < 1620 & ymin > 340 & ymin < 740')
                move_arround_while_firing()
            move()
            results = get_monster()
            data = results.pandas().xyxy[0]
            if len(data)<3:
                move(1)
        elapsed_time_one_minute = time()
        monster_killed_in_one_minute = 0
        

    if len(data) > 0:
        random_monster = results.pandas().xyxy[0].sample().to_dict('records')[0]
        monster_h = random_monster['ymax'] - random_monster['ymin']
        monster_w = random_monster['xmax'] - random_monster['xmin']
        x = random_monster['xmin'] + monster_w/2
        y = random_monster['ymin'] + (monster_h)/2
        pyautogui.moveTo(x, y)
        xmin = 0 if random_monster['xmin'] < 200 else random_monster['xmin'] - 200
        ymin = 0 if random_monster['ymin'] < 200 else random_monster['ymin'] - 200
        box_to_find_heal_bar_preshoot = ( xmin,  ymin, monster_w + 500, monster_h + 500)
        
        print("----Monster movement---")
        first_heal_bar = find_heal_bar()
        print(first_heal_bar)
        second_heal_bar = find_heal_bar()
        print(second_heal_bar)
        # if first_heal_bar and second_heal_bar:

        heal_bar = second_heal_bar
        if heal_bar is None:
            continue
        shooting = True
        pydirectinput.press('1')
        pyautogui.mouseDown(button="left")
        pydirectinput.press('5')
        pydirectinput.press('e')
        heal_box_while_shooting = (600, 300, 700, 400)
        heal_bar = pyautogui.locateOnScreen(heal_bar_img, region=heal_box_while_shooting,confidence=heal_confidence)
        loss_heal_bar = pyautogui.locateOnScreen(loss_heal_bar_img, region=heal_box_while_shooting,confidence=heal_confidence)
        if heal_bar is None:
            pyautogui.mouseUp(button="left")
            pyautogui.mouseUp(button="left")
            sleep(0.01)
            pydirectinput.press('1')
            continue


        start_shoot_time = time()
        while (heal_bar or loss_heal_bar) and time() - start_shoot_time < 7:
            heal_bar = pyautogui.locateOnScreen(heal_bar_img, region=heal_box_while_shooting,confidence=heal_confidence)
            loss_heal_bar = pyautogui.locateOnScreen(heal_bar_img, region=heal_box_while_shooting,confidence=heal_confidence)
            tctd = pyautogui.locateOnScreen('tctd.png', region=(245, 0, 580, 24), confidence=0.7)
            pydirectinput.press('e')
            # pydirectinput.press('shift')
            next_monsters = get_monster()
            if tctd is None:
                pydirectinput.press('1')
        pydirectinput.press('e')
        pyautogui.mouseUp(button="left")
        pyautogui.mouseUp(button="left")
        sleep(0.01)
        
        if loss_heal_bar is None and heal_bar is None:
            monster_killed += 1
            monster_killed_in_one_minute += 1
            print("Monster kill: {}".format(monster_killed))
        else:
            print("Found monster but not kill")
        pydirectinput.press('1')
        shooting = False

    # if time() - time_to_move > 30 and max_number_of_monster < min_limit_max_number_of_monster:
    #     move()
    #     time_to_move = time()
    #     max_number_of_monster = 0
