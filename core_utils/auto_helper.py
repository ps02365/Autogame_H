import pyautogui
import torch
from time import sleep, time
import pydirectinput
from .window_capture import WindowCapture
import cv2
import numpy as np

last_killed_at = None
running = True
revising = False
max_monster_count = 0
start_time_fetch_monster = time()

def auto_high_down():
    tick = 20
    yaxis = 275
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

def auto_ammunition():
    tick = 1
    while True:
        if running:
            use_ammunition_box()
        sleep(0.05)

def auto_socket():
    tick = 0.1
    while True:
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

def auto_skill_ig():
    tick = 0.1
    while True:
        if running:
            use_hyper_moving()
            use_ber()
        sleep(tick)

def auto_refuel():
    tick = 60
    while True:
        if running:
            recharge_fuel()
        sleep(tick)

def auto_detect_monster():
    model = torch.hub.load('.\\yolov7', 'custom', '.\\best.pt',  source='local')
    wincap = WindowCapture('DreamACE')
    global max_monster_count
    while True:
        if running:
            screen = wincap.get_screenshot()
            cropped_region = screen
            corrected_colors = cv2.cvtColor(cropped_region, cv2.COLOR_RGB2BGR)
            model.conf = 0.33
            results = model(corrected_colors)
            data = results.pandas().xyxy[0]
            if len(data) > max_monster_count:
                max_monster_count = len(data)

def use_ammunition_box():
    ammunition = pyautogui.locateOnScreen('out_of_ammunition.png', region=(0, 0, 300, 100), confidence=0.55)
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

def recharge_fuel():
    skill_socket = pyautogui.locateOnScreen('skill_socket.png', confidence=0.95)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("9")
        sleep(1)
        pydirectinput.press("9")
        sleep(1)