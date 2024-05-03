from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
import random
from datetime import datetime
from threading import Thread
import win32gui

powered_by =r"""
  __     __  ___       ____       ___  _____    __   _________  
 |  |   |  | \  \     /    \     /  / |     \  |  | |   ______|  
 |  |___|  |  \  \   /  /\  \   /  /  |  |\  \ |  | |  |  ____  
 |   ___   |   \  \ /  /  \  \ /  /   |  | \  \|  | |  | |_   | 
 |  |   |  |    \  V  /    \  V  /    |  |  \  \  | |  |___|  | 
 |__|   |__|     \___/      \___/     |__|   \____| |_________| 

"""

die_count = 0
current_slot = 2
last_killed_at = None
running = True
revising = False
start_die_time = time()
def start_game():
    print(powered_by)
    print ("Powered by Hwng")
    hwd = win32gui.FindWindow(None, "DreamACE")
    start_auto()


    
def start_auto():
    start_die_time = time()
    auto_skill_MG_process = Thread(target=auto_skill_MG, daemon=True)
    auto_skill_MG_process.start()

    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()

    auto_high_down_process = Thread(target=auto_high_down, daemon=True)
    auto_high_down_process.start()

    auto_refuel_process = Thread(target=auto_refuel, daemon=True)
    auto_refuel_process.start()

    rightmove = ((1920/8)*7)   
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
            # if time() - start_die_time > 1800:
            #     auto_die()
            #     sleep(1)
            #     start_die_time = time()
            #     sleep(1)
            # position_air_plane(i)
            pyautogui.moveTo(rightmove, 500)
        sleep(0.2)

    
def auto_die():
    global running
    pydirectinput.press("e")
    sleep(0.1)
    pyautogui.moveTo(960, 1080)
    try:
        revise_dialog = pyautogui.locateOnScreen('./1920x1080/dialog.png', confidence=0.6,grayscale= False)
    except:
        revise_dialog = None
    while not revise_dialog:
        pydirectinput.keyDown('space')
        sleep(0.5)
        pyautogui.moveTo(960, 1080)
        try:
            revise_dialog = pyautogui.locateOnScreen('./1920x1080/dialog.png', confidence=0.6,grayscale= False)
        except:
            revise_dialog = None
        check_for_revival()
    sleep(0.5)
    pydirectinput.keyUp('space')
    sleep(0.5)
    pydirectinput.press('s')
    sleep(0.5)

def auto_refuel():
    tick = 60
    while True:
        if running:
            recharge_fuel()
        sleep(tick)

def recharge_fuel():
    right = 1889     
    top = 255
    width = 19
    height = 60
    region_to_fetch = (right,top, width,height)
    try:
        skill_socket = pyautogui.locateOnScreen('./1920x1080/skill_socket.png', confidence=0.999,region=region_to_fetch,grayscale=False)
    except:
        skill_socket = None 
    if skill_socket:
        sleep(0.1)
        pydirectinput.keyDown("9")
        sleep(0.1)
        pydirectinput.keyUp("9")
        sleep(1)
        pydirectinput.keyDown("9")
        sleep(0.1)
        pydirectinput.keyUp("9")
        sleep(0.1)

def auto_high_up():
    while True:
        if running:
            sleep(120)
            high_up()
        sleep(0.1)

def high_up():
    tick = 1
    rightmove = ((1920/8)*7)   
    pyautogui.moveTo(rightmove, 440)
    sleep(tick)   
    pyautogui.moveTo(rightmove, 440)
    sleep(tick)
    pyautogui.moveTo(rightmove, 440)
    sleep(tick)

def auto_high_down():
    tick = 1
    left = 1889     
    top = 255
    width = 19
    height = 60
    region_to_fetch = (left,top, width,height)
    sleep(15)
    global running
    while True:
        if revising == False:
            try: 
                high_point = pyautogui.locateOnScreen('./1920x1080/current_height_2.png', confidence=0.9,region=region_to_fetch,grayscale= False)
            except:
                high_point = None
            if not high_point:
                running = False
                sleep(3)
                pydirectinput.keyDown("s")
                # pydirectinput.keyDown("space")
                while not high_point:
                    pyautogui.moveTo(1900, 600)
                    sleep(1)
                    pyautogui.moveTo(1900, 540)
                    try:
                        high_point = pyautogui.locateOnScreen('./1920x1080/current_height_2.png', confidence=0.9,region=region_to_fetch,grayscale= False)
                    except:
                        high_point = None
                # pydirectinput.keyUp("space")
                running = True
        sleep(tick)

def auto_skill_IG():
    tick = 0.01
    region_fetch_socket = (245, 0, 1000, 24)
    while True:
        if running:
            try:
                skill_socket = pyautogui.locateOnScreen('./1920x1080/skill_socket.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                skill_socket = None
            if skill_socket == None:
                sleep(0.1)
                pydirectinput.keyDown("9")
                sleep(0.1)
                pydirectinput.keyUp("9")
                sleep(1)
            try:
                kit_socket = pyautogui.locateOnScreen('./1920x1080/kit_socket.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                kit_socket = None
            if kit_socket == None:
                sleep(0.1)
                pydirectinput.keyDown("0")
                sleep(0.1)
                pydirectinput.keyUp("0")
                sleep(1)
            try:
                Ber = pyautogui.locateOnScreen('./1920x1080/Ber.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                Ber = None
            if Ber == None:
                sleep(0.1)
                pydirectinput.keyDown("6")
                sleep(0.1)
                pydirectinput.keyUp("6")
                sleep(1)
        sleep(tick)
        

def auto_skill_MG():
    tick = 0.01
    region_fetch_socket = (245, 0, 1000, 24)
    while True:
        if running:
            try:
                skill_socket = pyautogui.locateOnScreen('./1920x1080/skill_socket.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                skill_socket = None
            if skill_socket == None:
                sleep(0.1)
                pydirectinput.keyDown("9")
                sleep(0.1)
                pydirectinput.keyUp("9")
                sleep(1)
            try:
                kit_socket = pyautogui.locateOnScreen('./1920x1080/kit_socket.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                kit_socket = None
            if kit_socket == None:
                sleep(0.1)
                pydirectinput.keyDown("0")
                sleep(0.1)
                pydirectinput.keyUp("0")
                sleep(1)
            # try:
            #     phukien_socket = pyautogui.locateOnScreen('./1920x1080/phukien_socket.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            # except:
            #     phukien_socket = None
            # if phukien_socket == None:
            #     sleep(0.1)
            #     pydirectinput.keyDown("0")
            #     sleep(0.1)
            #     pydirectinput.keyUp("0")
            #     sleep(1)
            try:
                Save_SP = pyautogui.locateOnScreen('./1920x1080/Save_SP.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                Save_SP = None
            if Save_SP == None:
                sleep(0.1)
                pydirectinput.keyDown("4")
                sleep(0.1)
                pydirectinput.keyUp("4")
                sleep(1)
            try:
                Buff_1 = pyautogui.locateOnScreen('./1920x1080/Buff_1.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                Buff_1 = None
            if Buff_1 == None:
                sleep(0.1)
                pydirectinput.keyDown("5")
                sleep(0.1)
                pydirectinput.keyUp("5")
                sleep(1)
            try:
                Buff_2 = pyautogui.locateOnScreen('./1920x1080/Buff_2.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                Buff_2 = None
            if Buff_2 == None:
                sleep(0.1)
                pydirectinput.keyDown("6")
                sleep(0.1)
                pydirectinput.keyUp("6")
                sleep(1)
            try:
                Buff_3 = pyautogui.locateOnScreen('./1920x1080/Buff_3.png', confidence=0.999, region=region_fetch_socket,grayscale=False)
            except:
                Buff_3 = None
            if Buff_3 == None:
                sleep(0.1)
                pydirectinput.keyDown("7")
                sleep(0.1)
                pydirectinput.keyUp("7")
                sleep(1)               
        sleep(tick)

def check_for_revival():
    try:
        button7location = pyautogui.locateOnScreen('./1920x1080/dialog.png', confidence=0.6,grayscale=False)
    except:
        button7location = None
    global running
    global revising
    if button7location:
        running = False
        revising = True
        sleep(0.1)
        pydirectinput.press("a")
        sleep(0.1)
        pydirectinput.press("e")
        sleep(0.1)
        pydirectinput.press("s")
        sleep(0.1)
        pydirectinput.press('esc')
        sleep(1)
        # go_to_s2()
        go_to_s1_redline
        revising = False
        running = True
        # slots = [
        #     'go_to_s2',
        #     'go_to_s5']
        # slot_to_go = random.choice(slots)
        # eval(f"{slot_to_go}()")

# def go_to_s4():
#     sleep(1.5)
#     pyautogui.moveTo(955, 547)
#     sleep(0.1)
#     pydirectinput.press('w')
#     sleep(5)
#     pyautogui.moveTo(0, 540)
#     sleep(0.5)
#     pyautogui.moveTo(960, 540)
#     sleep(5)
#     pyautogui.moveTo(960, 540)
#     sleep(10)

def go_to_s1_redline():
    pydirectinput.keyDown('space')
    sleep(1)
    pyautogui.moveTo((1920/10)*5.5, 540)
    sleep(2.5)    
    pydirectinput.keyUp('space')
    sleep(0.5)
    pydirectinput.keyDown('s')

def go_to_s3_redline():
    pyautogui.moveTo((1920/8)*5, 540)
    sleep(2)
    pyautogui.moveTo(960, 540)
    sleep(0.5)
    pydirectinput.keyDown('space')
    sleep(10)
    pydirectinput.keyUp('space')
    sleep(0.5)
    pydirectinput.keyDown('s')
    
def go_to_s2():
    pydirectinput.keyDown('space')
    sleep(2.5)
    pyautogui.moveTo(955, 560)
    sleep(2)
    pyautogui.moveTo((1920/8)*2.4, 580)
    sleep(1.5)
    pydirectinput.keyUp('space')
    sleep(0.5)
    pyautogui.moveTo(960, 535)
    sleep(0.5)
    pydirectinput.keyDown('s')

def go_to_s5():
    pydirectinput.keyDown('space')
    sleep(2.5)
    pyautogui.moveTo(955, 560)
    sleep(12)
    pydirectinput.keyUp('space')
    sleep(0.5)
    pydirectinput.keyDown('s')

# def go_to_s3():
#     sleep(1.5)
#     pyautogui.moveTo(920, 630)
#     sleep(0.1)
#     pydirectinput.press('w')
#     sleep(1.5)
#     pyautogui.moveTo(970, 570)
#     sleep(0.5)

# def go_to_s5():
#     sleep(1.5)
#     pydirectinput.press('w')
#     sleep(0.1)
#     pydirectinput.press('w')
#     pyautogui.moveTo(960, 560)
#     sleep(14)


# def go_to_s6():
#     sleep(1.5)
#     pyautogui.moveTo(960, 560)
#     sleep(0.1)
#     pydirectinput.press('w')
#     sleep(1)
#     pyautogui.moveTo(1920, 540)
#     sleep(0.65)
#     pyautogui.moveTo(960, 540)
#     sleep(8)
#     pyautogui.moveTo(480, 540)
#     pydirectinput.keyDown('r')
#     sleep(0.5)
#     pydirectinput.keyUp('r')
#     sleep(2)
#     pyautogui.moveTo(960, 540)
#     sleep(2)

# def go_to_s9():
#     height_go_up = 490
#     height_blance = 540
#     height_go_down = 600
#     sleep(1.5)
#     pyautogui.moveTo(960, height_go_up)
#     sleep(0.1)
#     pydirectinput.press('w')
#     sleep(1)
#     pydirectinput.keyDown('a')
#     pyautogui.moveTo(1920, height_go_up)
#     sleep(0.25)
#     pydirectinput.keyUp('a')
#     pyautogui.moveTo(960, height_blance)
#     sleep(13)
#     pyautogui.moveTo(960, height_go_down)
#     sleep(8.5)
    


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

def auto_ammunition():
    tick = 1
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

def position_air_plane(i = -1):
    right_move = 1680
    pyautogui.moveTo(right_move, 535)
    sleep(0.1)

def run_air_plane():
    sleep(0.1)
    pydirectinput.press('c')
    sleep(0.1)

start_game()
