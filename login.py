import pyautogui
import time
import pydirectinput
from datetime import datetime
from ReadWriteMemory import ReadWriteMemory

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False
rwm = ReadWriteMemory()
image_folder = "1920x1080"
confirm_disconnect_dialog_image_path = f"{image_folder}/confirm_disconnect_dialog.PNG"
choose_air_plane_btn_image_path = f"{image_folder}/choose_air_plane_btn.PNG"
city_title_image_path = f"{image_folder}/city_title.png"
disconnect_detect_image_path = f"{image_folder}/disconnect_detect.PNG"
map_to_afk_image_path = f"{image_folder}/map_to_afk.PNG"
stopped_airplane_image_path = f"{image_folder}/stopped_airplane.PNG"
confirm_stop_image_path = f"{image_folder}/confirm_stop.PNG"
ev_map_position = (1108, 993)
fetch_map_region = (1554, 0, 366, 19)

def login(fov_addr):
    pydirectinput.press("shift")
    time.sleep(0.3)
    pyautogui.mouseUp()
    login_screen = detect_disconnect()
    while login_screen:
        confirm_disconnect_dialog_btn = pyautogui.locateOnScreen(confirm_disconnect_dialog_image_path, confidence=0.9)
        while confirm_disconnect_dialog_btn:
            pyautogui.click(confirm_disconnect_dialog_btn[0], confirm_disconnect_dialog_btn[1])
            time.sleep(1)
            pyautogui.moveTo(0,0)
            confirm_disconnect_dialog_btn = pyautogui.locateOnScreen(confirm_disconnect_dialog_image_path, confidence=0.9)
        time.sleep(1)
        pydirectinput.press("enter")
        time.sleep(5)
        login_screen = detect_disconnect()
    print(datetime.now(), " Finish login")            
    choose_air_plane_btn = pyautogui.locateOnScreen(choose_air_plane_btn_image_path, confidence=0.8)
    while not choose_air_plane_btn:
        choose_air_plane_btn = pyautogui.locateOnScreen(choose_air_plane_btn_image_path, confidence=0.8)
        time.sleep(0.5)
    pydirectinput.press("enter")

    # Should see city title
    pyautogui.click(choose_air_plane_btn[0], choose_air_plane_btn[1])
    city_title = pyautogui.locateOnScreen(city_title_image_path, confidence=0.6, region=fetch_map_region)
    while not city_title:
        pyautogui.click(choose_air_plane_btn[0], choose_air_plane_btn[1])
        time.sleep(2)
        city_title = pyautogui.locateOnScreen(city_title_image_path, confidence=0.6, region=fetch_map_region)
    print(datetime.now(), " See the city")

    # See all
    process = rwm.get_process_by_name("SF_Main.exe")
    process.open()
    fov_ptr = process.get_pointer(fov_addr)
    time.sleep(0.5)
    process.write(fov_ptr, -180)
    

    # Should AFK map
    pyautogui.click(ev_map_position[0], ev_map_position[1])
    time.sleep(1)
    map_to_afk = pyautogui.locateOnScreen(map_to_afk_image_path, confidence=0.6, region=fetch_map_region)

    while not map_to_afk:
        pyautogui.click(ev_map_position[0], ev_map_position[1])
        time.sleep(1)
        map_to_afk = pyautogui.locateOnScreen(map_to_afk_image_path, confidence=0.6, region=fetch_map_region)
        
    time.sleep(1)
    process.write(fov_ptr, 120)
    print(datetime.now(), " See the event map")
    print(datetime.now(), " Finish login")
    process.close()

def from_city_go_to_ev():
    pass

def detect_disconnect():
    return pyautogui.locateOnScreen(disconnect_detect_image_path, confidence=0.8)








