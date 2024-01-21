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
    Not_Training_area_test()
    # start_die_time = time()

    # auto_ammunition_process = Thread(target=auto_ammunition, daemon=True)
    # auto_ammunition_process.start()

    # auto_auto_high_up = Thread(target=auto_high_up, daemon=True)
    # auto_auto_high_up.start()

    # auto_high_down_process = Thread(target=auto_high_down, daemon=True)
    # auto_high_down_process.start()

    # run_air_plane()
    # fire()
    # speed_down_air_plane()
    # position_air_plane()
    # for i in range(100000000):
    #     check_for_revival()
    #     if running:
    #         eval("{}()".format(move_function_name))
    #         if i % 2 == 0:
    #             release_fire()
    #             release_down_air_plane()
    #             if time() - start_die_time > 600:
    #                 auto_die()
    #                 start_die_time = time() 
    #             eval("{}()".format(move_function_name))   
    #     sleep(0.2)

# def Training_area():
#     global running
#     while True:
#         if revising == False:
#             try:
#                 Training_area_1 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(700,280,870,380)) #s7
#                 Training_area_2 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(960,300,1040,370)) #s8
#                 Training_area_3 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(1060,550, 1175,625)) #s6
#                 Training_area_4 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(690,600, 1020,800)) #s1,2
#             except:
#                 Training_area_1 = None
#                 Training_area_2 = None
#                 Training_area_3 = None
#                 Training_area_4 = None
#             if not Training_area_1 or Training_area_2 or Training_area_3 or Training_area_4:
#                 running = False
#                 while not Training_area_1 or Training_area_2 or Training_area_3 or Training_area_4:
#                     auto_die()
#                     Training_area_1 or Training_area_2 or Training_area_3 or Training_area_4
#                 running = True
#             sleep (300)   

def screenshot():
    right = 980     
    top = 620
    width = 240
    height = 180
    region_to_fetch = (right,top,width,height)
    pyautogui.screenshot("Not_Trainning_Area_1.png",region_to_fetch) 

def Not_Training_area():
    global running

    while True:
        if revising == False:
            try:
                Not_Training_area_1 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(850,280,375,260),grayscale= False) #s8,s9,s5,s6
                Not_Training_area_2 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(805,350,150,260),grayscale= False) #s4
                Not_Training_area_3 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(980,620,240,180),grayscale= False) #s3
            except:
                Not_Training_area_1 = None
                Not_Training_area_2 = None
                Not_Training_area_3 = None         
            if Not_Training_area_1 or Not_Training_area_2 or Not_Training_area_3:
                running = False
                while Not_Training_area_1 or Not_Training_area_2 or Not_Training_area_3:
                    auto_die()
                    not Not_Training_area_1 or Not_Training_area_2 or Not_Training_area_3
                running = True
            sleep (5)   


def Not_Training_area_test():
    global running
    while True:
        if revising == False:
            print(1)
            try:
                Not_Training_area_1 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(850,280,375,260),grayscale= False) #s8,s9,s5,s6
                Not_Training_area_2 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.9,region=(805,350,150,260),grayscale= False) #s4
                Not_Training_area_3 = pyautogui.locateOnScreen('./1920x1080/Air_Plane.png', confidence=0.2,region=(980,620,240,180),grayscale= False) #s3
            except:

                Not_Training_area_1 = None
                Not_Training_area_2 = None
                Not_Training_area_3 = None         
            print(1.1)
            if Not_Training_area_3:
                print(2)
                running = False
                print(3)
                while Not_Training_area_3:
                    print(4)
                    auto_die()
                    print(5)
                    not Not_Training_area_3
                    print(6)
                running = True
                print(7)
            sleep (5)   

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
    top = 293
    right = 1889
    width = 19
    height = 23
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
                while not high_point:
                    pyautogui.moveTo(1920, 700)
                    sleep(1)
                    pyautogui.moveTo(1920, 540)
                    try:
                        high_point = pyautogui.locateOnScreen('./1920x1080/current_height_2.png', confidence=0.9,region=region_to_fetch,grayscale= False)
                    except:
                        high_point = None
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
        ammunition = pyautogui.locateOnScreen('./1920x1080/out_of_ammunition.png', confidence=0.6,grayscale= False)
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
