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


def open_inventoy():
    pydirectinput.keyDown('b')
    sleep(0.1)
    pydirectinput.keyUp('b')
    sleep(0.1)
    pyautogui.click(left_1+15,top_1+20) #click dừng
    sleep(0.1)
    pydirectinput.keyDown("i")    
    sleep(0.01)
    pydirectinput.keyUp("i")    
    sleep(0.5)

def locate_image_inventory():
    left = 1000     
    top = 670
    width = 200
    height = 200
    region_to_fetch = (left,top,width,height)
    try:
        inventory = pyautogui.locateOnScreen('./1920x1080/arrange.png',region=region_to_fetch, confidence=0.7,grayscale=False)
        if inventory is not None:
            return inventory
    except Exception as e:
        print("Not Found Inventory", e)
        return None


def locate_image_tick():
    left = 640     
    top = 432
    width = 640
    height = 216
    region_to_fetch = (left,top,width,height)
    try:
        tick = pyautogui.locateOnScreen('./1920x1080/tick.png', region = region_to_fetch, confidence=0.6,grayscale=False)
        if tick is not None:
            return tick
    except Exception as e:
        print("Not Found Tick", e)
        return locate_image_tick()

def Stop():
    # pydirectinput.keyDown('b')
    # sleep(0.1)
    # pydirectinput.keyUp('b')
    # sleep(0.1)
    image_position_tick = locate_image_tick()
    if image_position_tick:
        left_1, top_1, width_1, height_1 = image_position_tick
    # pyautogui.click(left_1+15,top_1+20) 
    # sleep(0.05)
    # pydirectinput.keyDown("i")    
    # sleep(0.05)
    # pydirectinput.keyUp("i")    

def Accuracy():
    # Stop()
    # sleep(0.05)
    image_position_inventory = locate_image_inventory()
    if image_position_inventory:
        print("Image found at:", image_position_inventory)
        left_2, top_2, width_2, height_2 = image_position_inventory 
    pyautogui.moveTo(left_2-170,top_2-225)
    sleep(1)
    pyautogui.moveTo(left_2-200,top_2-225)
    sleep(1)
    pyautogui.moveTo(left_2-200,top_2-200)
    sleep(1)
    pyautogui.moveTo(left_2-170,top_2-200)

if __name__ == "__main__":
    # hwd = win32gui.FindWindow(None, "DreamACE")
    # if not hwd:
    #     exit()
    # win32gui.SetForegroundWindow(hwd)
    sleep(0.1)
    # Accuracy()
    Stop()

