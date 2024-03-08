from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
# from core_utils.window_capture import WindowCapture
from threading import Thread

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False


die_count = 0
current_slot = 2
last_killed_at = None
running = True
revising = False
start_die_time = time()
# auto_die_time_elapsed = time()
# wincap = WindowCapture('DreamACE')
move_function_name = 'position_air_plane'
def start_game():
    gw.getWindowsWithTitle('DreamACE')[0].activate()
    sleep(1)

    start_auto()

def start_auto():
    # screenshot()
    #start_die_time = time()

    auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    auto_ammunition_process.start()

    # auto_auto_high_up = Thread(target=auto_high_up, daemon=True)
    # auto_auto_high_up.start()

    auto_high_down_process = Thread(target=auto_high_down, daemon=True)
    auto_high_down_process.start()

    run_air_plane()
    fire()
    speed_down_air_plane()
    position_air_plane()
    for i in range(100000000):
        check_for_revival()
        if running:
            eval("{}()".format(move_function_name))
            if i % 2 == 0:
                release_fire()
                release_down_air_plane()
                # if time() - start_die_time > 600:
                #     auto_die()
                #     sleep(0.5)
                #     start_die_time = time()
                #     sleep(0.5)
                # eval("{}()".format(move_function_name))   
        sleep(0.2)

def screenshot():
    right = 1889     
    top = 300
    width = 19
    height = 16
    region_to_fetch = (right,top,width,height)
    pyautogui.screenshot("Not_Trainning_Area_1.png",region_to_fetch) 

def auto_die():
    global running
    # running = False
    # sleep(4)
    # try:
    #     skill_socket = pyautogui.locateOnScreen('./1920x1080/kit_socket.png', confidence=0.95)
    # except:
    #     skill_socket = None
    # if skill_socket:
    #     sleep(0.1)
    #     pydirectinput.press("0")
    #     sleep(1)
    # sleep(0.1)
    # pydirectinput.press("a")
    # sleep(0.1)
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

def check_for_revival():
    try:
        button7location = pyautogui.locateOnScreen('./1920x1080/dialog.png', confidence=0.6,grayscale=False)
    except:
        button7location = None
    # global current_slot
    # global die_count
    # global last_killed_at
    global running
    global revising
    # global start_time_fetch_monster
    # global max_monster_count
    if button7location:
        running = False
        revising = True
        # start_time_fetch_monster = time()
        # max_monster_count = 0
        # die_count += 1
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
    right = 1889
    top = 298
    width = 19
    height = 18
    region_to_fetch = (right,top, width,height)
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
                pydirectinput.keyDown("space")
                while not high_point:
                    pyautogui.moveTo(1920, 650)
                    sleep(1)
                    pyautogui.moveTo(1920, 540)
                    try:
                        high_point = pyautogui.locateOnScreen('./1920x1080/current_height_2.png', confidence=0.9,region=region_to_fetch,grayscale= False)
                    except:
                        high_point = None
                pydirectinput.keyUp("space")
                running = True
        sleep(tick)

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

def speed_down_air_plane():
    sleep(0.1)
    pydirectinput.keyDown("s")
    sleep(0.05)
    pydirectinput.keyDown("a")
    sleep(0.1)

def position_air_plane():
    right_move = ((1920/8)*7)
    pyautogui.moveTo(right_move, 540)
    sleep(0.1)

def run_air_plane():
    pyautogui.moveTo(960, 540)
    sleep(0.1)
    pydirectinput.press('w')
    sleep(0.1)

start_game()
