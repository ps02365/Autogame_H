from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
import random
from datetime import datetime
from threading import Thread, Event
import cv2
import numpy as np
import win32gui
import configparser
default_config_mouse_location = {
    "high_down_mouse_points": [(1920, 700), (1920, 540)],
    "auto_die_mouse_move":(960, 1080),
    "region_fetch_socket": (245, 0, 580, 24),
    "position_air_plane_point": (1700, 540)
}
config = configparser.ConfigParser()
config.read("config.ini")
config.sections()

high_down_enable = bool(config["DEFAULT"]["high_down_enable"])
high_down_fetch_box = eval(config["DEFAULT"]["high_down_fetch_box"])
auto_die_enable = bool(config["DEFAULT"]["auto_die_enable"])
resolution = config["DEFAULT"]["resolution"]

dialog_image_path = f'{resolution}/dialog.PNG'
out_of_ammunition_image_path = f'{resolution}/out_of_ammunition.png'
skill_socket_image_path = f'{resolution}/skill_socket.png'
current_height_image_path = f'{resolution}/current_height.png'
kit_socket_image_path = f'{resolution}/kit_socket.png'
start_die_time = time()

running_event = Event()
def start_game():
    hwnd = win32gui.FindWindow(None, "DreamACE")
    if not hwnd:
        raise Exception("Not found DreamACE window")
    win32gui.SetForegroundWindow(hwnd)
    sleep(1)
    
    start_auto()
    # go_to_s6()
    

def auto_die():
    if not auto_die_enable:
        return
    
    while running_event.is_set():
        running_event.clear()
    sleep(4)
    kit_socket = pyautogui.locateOnScreen('kit_socket.png', confidence=0.95, region=default_config_mouse_location["region_fetch_socket"])
    if kit_socket:
        sleep(0.1)
        pydirectinput.press("0")
        sleep(1)

    sleep(0.1)
    pydirectinput.press("a")
    sleep(0.1)
    pydirectinput.press("e")
    sleep(0.1)
    pyautogui.moveTo(*default_config_mouse_location["auto_die_mouse_move"])
    revise_dialog = pyautogui.locateOnScreen('dialog.png', confidence=0.6)
    pydirectinput.keyDown('space')
    while not revise_dialog:
        sleep(0.5)
        pyautogui.moveTo(*default_config_mouse_location["auto_die_mouse_move"])
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


    run_air_plane()
    position_air_plane()
    speed_down_air_plane()
    fire()
    for i in range(100000000):
        check_for_revival()
        if running_event.is_set():
            position_air_plane()
            if i % 2 == 0:
                release_fire()
                release_down_air_plane()
            position_air_plane()
            if time() - start_die_time > 600:
                auto_die()
            position_air_plane()
        sleep(0.2)

def recharge_fuel():
    skill_socket = pyautogui.locateOnScreen('skill_socket.png', confidence=0.99)
    if skill_socket:
        sleep(0.1)
        pydirectinput.press("9")
        sleep(1)
        pydirectinput.press("9")
        sleep(1)

def auto_high_down():
    tick = 10
    while True:
        if high_down_enable:
            high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.5,region=high_down_fetch_box)
            if not high_point:
                while running_event.is_set():
                    running_event.clear()
                sleep(3)
                pydirectinput.keyDown("s")
                while not high_point:
                    pyautogui.moveTo(1920, 700)
                    sleep(1)
                    pyautogui.moveTo(1920, 540)
                    high_point = pyautogui.locateOnScreen('current_height.png', confidence=0.5,region=high_down_fetch_box)

                while not running_event.is_set():
                    running_event.set()
            sleep(tick)
            

def auto_ammunition():
    while True:
        if running_event.is_set():
            use_ammunition_box()
        sleep(0.02)

def auto_skill():
    tick = 5
    region_fetch_socket = default_config_mouse_location["region_fetch_socket"]
    while True:
        if running_event.is_set():
            skill_socket = pyautogui.locateOnScreen(skill_socket_image_path,confidence=0.999, region=region_fetch_socket)
            if skill_socket == None:
                sleep(0.1)
                pydirectinput.press("9")
                sleep(1)
            kit_socket = pyautogui.locateOnScreen(kit_socket_image_path, confidence=0.999, region=region_fetch_socket)
            if kit_socket == None:
                sleep(0.1)
                pydirectinput.press("0")
                sleep(1)
                
        sleep(tick)

def auto_refuel():
    tick = 60
    while True:
        if running_event.is_set():
            recharge_fuel()
        sleep(tick)

def check_for_revival():
    global start_die_time
    button7location = pyautogui.locateOnScreen('dialog.png', confidence=0.6)
    if button7location:
        start_die_time = time()
        while running_event.is_set():
            running_event.clear()
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
        while not running_event.is_set():
            running_event.set()

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
    ammunition = pyautogui.locateAllOnScreen('out_of_ammunition.png', confidence=0.4)
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

def speed_down_air_plane():
    sleep(0.1)
    pydirectinput.keyDown("s")
    sleep(0.05)
    pydirectinput.keyDown("a")
    sleep(0.1)

def position_air_plane():
    pyautogui.moveTo(*default_config_mouse_location["position_air_plane_point"])
    sleep(0.1)

def run_air_plane():
    sleep(0.1)
    pydirectinput.press('w')
    sleep(0.1)

if __name__ == "__main__":
    start_game()
