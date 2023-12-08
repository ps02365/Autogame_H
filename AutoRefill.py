import pyautogui
import pydirectinput
import pygetwindow as gw
from time import sleep

class AutoRefill:
    REFILL_POSITION_IN_FRONT_OF_IF = 'in_front_of_if'
    REFILL_POSITION_OPPOSITE_IF_RIGHT = 'opposite_if_right'
    step_to_warp = 6
    elevator_forward_y_plus = 150
    warp_forward_y_plus = 120
    pyautogui.FAILSAFE = False
    def move_from_in_front_of_if(self):
        #Get refill position
        x, y = pyautogui.size()
        center_x = x/2
        center_y = y/2
        elevator1 = pyautogui.locateOnScreen('elevator_1.png', confidence=0.6)
        elevator2 = pyautogui.locateOnScreen('elevator_2.png', confidence=0.6)
        count = 0
        #Check elevator
        while elevator1 is None and count <= 60 and elevator2 is None:
            count += 1
            pyautogui.moveTo(center_x - 40, center_y)
            sleep(0.1)
            pyautogui.mouseDown(button='right')
            pyautogui.moveTo(center_x, center_y, 1)
            pyautogui.mouseUp(button='right')
            sleep(0.1)
            elevator1 = pyautogui.locateOnScreen('elevator_1.png', confidence=0.6)
            sleep(0.3)
            elevator2 = pyautogui.locateOnScreen('elevator_2.png', confidence=0.6)
            sleep(0.1)

        if count > 60:
            self.go_to_bark_and_return()
            return

        #Go to elevator
        if elevator1 is not None:
            pyautogui.moveTo(elevator1.left + 100, elevator1.top + 15)
            sleep(0.1)
            pyautogui.click()
            sleep(10)
        elif elevator2 is not None:
            pyautogui.moveTo(elevator2.left + 150, elevator2.top + 15)
            sleep(0.1)
            pyautogui.click()
            sleep(10)

        #Go forward
        for i in range(5):
            pyautogui.moveTo(center_x, center_y+elevator_forward_y_plus)
            sleep(0.1)
            pyautogui.click()
            sleep(1)

        above_wp_shop = pyautogui.locateOnScreen('above_wp_shop.png', confidence=0.6)
        while above_wp_shop is None:
            pyautogui.moveTo(center_x - 20, center_y)
            sleep(0.1)
            pyautogui.mouseDown(button='right')
            pyautogui.moveTo(center_x, center_y, 1)
            pyautogui.mouseUp(button='right')
            above_wp_shop = pyautogui.locateOnScreen('above_wp_shop.png', confidence=0.6)
            sleep(0.5)

        # #Go forward
        for i in range(step_to_warp):
            pyautogui.moveTo(center_x+30, center_y+warp_forward_y_plus)
            sleep(0.1)
            pyautogui.click()
            sleep(1)

        for i in range(10):
            pyautogui.moveTo(center_x-400, center_y+300)
            sleep(0.1)
            pyautogui.click(button='left')
            sleep(0.3)
        sleep(10)
            

    def move_from_opposite_if_right(self):
        x, y = pyautogui.size()
        center_x = x/2
        center_y = y/2
        pyautogui.moveTo(center_x - 200, center_y - 50)   
        sleep(0.1)
        pyautogui.click()
        sleep(10)
        self.move_from_in_front_of_if()

    def refill(self):
        refill_position = ""
        # move_from_in_front_of_if()
        if pyautogui.locateOnScreen('in_front_of_if.png', confidence=0.5) or pyautogui.locateOnScreen('in_front_of_if_1.png', confidence=0.5):
            self.move_from_in_front_of_if()
        elif pyautogui.locateOnScreen('opposite_if_right.png', confidence=0.6):
            global elevator_forward_y_plus
            elevator_forward_y_plus = 180
            global warp_forward_y_plus
            warp_forward_y_plus = 125
            global step_to_warp
            step_to_warp = 5
            self.move_from_opposite_if_right()
        else:
            self.go_to_bark_and_return()

    def go_to_bark_and_return(self):
        pyautogui.click(923, 991,button="left")
        sleep(5)
        pydirectinput.press('esc')
        sleep(5)
        pydirectinput.press('5')
        sleep(10)
        self.start()


    def start(self):
        gw.getWindowsWithTitle('DreamACE')[0].activate()
        sleep(1)
        # move_from_in_front_of_if()
        # return
        noti_refill = pyautogui.locateOnScreen('refill.png', confidence=0.55)
        while noti_refill is None:
            sleep(2)
            noti_refill = pyautogui.locateOnScreen('refill.png', confidence=0.55)
        sleep(2)
        pyautogui.moveTo(951, 766)
        pyautogui.click()
        self.refill()
         
    start()