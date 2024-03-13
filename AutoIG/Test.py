from time import sleep, time
import pyautogui
import pydirectinput
import pygetwindow as gw
from plyer import notification

pyautogui.FAILSAFE = False
pydirectinput.FAILSAFE = False


# def start_game():
#     gw.getWindowsWithTitle('DreamACE')[0].activate()
#     sleep(1)

#     start_auto()


# def start_auto():
#     screenshot()

# def screenshot():
#     right = 1889     
#     top = 252
#     width = 19
#     height = 63
#     region_to_fetch = (right,top,width,height)
#     pyautogui.screenshot("Test_screenshot.png",region_to_fetch) 
    
# start_game()




# Notification title and message
title = "Notification Title"
message = "abc!"

# Display the notification
notification.notify(
    title=title,
    message=message,
    timeout=2  # Notification will disappear after 10 seconds
)