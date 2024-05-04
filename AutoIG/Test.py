from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
from plyer import notification
import hashlib
import os
import wmi
import getpass
import win32gui
import random

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False


# def start_game():
#     gw.getWindowsWithTitle('DreamACE')[0].activate()
#     sleep(1)

#     start_auto()

# def start_auto():
#     screenshot()

   
# start_game()

#### Test license key

# def generate_license_key(device_id, secret_key):
#     data = device_id.encode() + secret_key.encode()
#     license_key = hashlib.sha256(data).hexdigest()
#     return license_key

# # Example usage:
# device_id = "example_device_id"
# secret_key = "example_secret_key"
# license_key = generate_license_key(device_id, secret_key)
# print("License Key:", license_key)




# def get_device_id():
#     return os.getenv('COMPUTERNAME')

# if __name__ == "__main__":
#     device_id = get_device_id()
#     print("Device ID:", device_id)





# def get_drive_serial_number():
#     c = wmi.WMI()
#     for drive in c.Win32_DiskDrive():
#         return drive.SerialNumber.strip()

# def generate_hash(device_id):
#     sha256 = hashlib.sha256()
#     sha256.update(device_id.encode())
#     hashed_device_id = sha256.hexdigest()
#     return hashed_device_id

# def checkkey(nhapkey, key):
#     if nhapkey == key:
#         print ('hợp lệ')
#         return
#     print('không hợp lệ')

# if __name__ == "__main__":
#     drive_serial_number = get_drive_serial_number()
#     print("Drive Serial Number:", drive_serial_number)
#     text_without_periods = drive_serial_number.replace('.', '')
#     encrypted_script = generate_hash(text_without_periods)
#     print("Encrypted script:", encrypted_script)
#     key = encrypted_script
#     nhapkey = getpass.getpass('')
#     checkkey(nhapkey, key)


def screenshot2():
    left = 1100     
    top = 670
    width = 200
    height = 200
    region_to_fetch = (left,top,width,height)
    pyautogui.screenshot("Test_screenshot_2.png",region = region_to_fetch)


def check_for_revival():
    try:
        button7location = pyautogui.locateOnScreen('./1920x1080/dialog.png', confidence=0.6,grayscale=False)
    except:
        button7location = None
    global running
    global revising
    if button7location:
        print(1)
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
        go_to_s3_redline
        revising = False
        running = True
        # slots = [
        #     'go_to_s3_redline',
        #     'go_to_s1_redline']
        # slot_to_go = random.choice(slots)
        # eval(f"{slot_to_go}()")

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

def go_to_s1_redline():
    pydirectinput.keyDown('space')
    sleep(1)
    pyautogui.moveTo((1920/10)*5.5, 540)
    sleep(2.5)    
    pydirectinput.keyUp('space')
    sleep(0.5)
    pydirectinput.keyDown('s')

if __name__ == "__main__":
    hwd = win32gui.FindWindow(None, "DreamACE")
    if not hwd:
        exit()
    win32gui.SetForegroundWindow(hwd)
    sleep(1)
    print (1)
    check_for_revival()
    print (2)
