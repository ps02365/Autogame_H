import cv2 as cv
import numpy as np
import os
from time import time,sleep
from core_utils.window_capture import WindowCapture
import pyautogui
import random

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('DreamACE')
# initialize the Vision class

cascade_monster = cv.CascadeClassifier('cascade/cascade.xml')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    # rectangles = cascade_monster.detectMultiScale(
    #     image=screenshot,
    #     # scaleFactor=5,
    #     # minNeighbors=4,
    #     # minSize=(50,50),
    #     # maxSize=(120,120)
    # )
    # detection_image = vision.draw_rectangles(screenshot, rectangles)
    # if len(rectangles) > 0:
    #     rectangle_idx = random.randrange(0, len(rectangles))
    #     rectangle = rectangles[rectangle_idx]
    #     print("rect", rectangle)
    #     pyautogui.moveTo(rectangle[0] + rectangle[2]/ 2, rectangle[1] + rectangle[3]/2)


    cv.imshow("Computer Vision", screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))        
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    # cv.imwrite('positive/night/{}.jpg'.format(loop_time), screenshot)
    sleep(1)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')