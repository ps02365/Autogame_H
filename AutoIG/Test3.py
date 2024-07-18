from time import sleep
import pyautogui
import configparser


pyautogui.FAILSAFE = False

def locate_image_arrange():
    left = 900     
    top = 650
    width = 300
    height = 220
    region_to_fetch = (left, top, width, height)
    try:
        inventory = pyautogui.locateOnScreen('./1920x1080/arrange.png', confidence=0.7, grayscale=False)
        if inventory is not None:
            return inventory
    except pyautogui.ImageNotFoundException as e:
        print("Arrange image not found:", e)

def slot_1(left_1, top_1):
    image_position_inventory = locate_image_arrange()
    if image_position_inventory:
        left, top, width, height = image_position_inventory
        left_1 = left-300
        top_1 = top-200
    else:
        print("Unable to locate slot_1.")
    return left_1, top_1

def slot_2(left_2, top_2):
    left_2 = left_1+30
    top_2 = top_1
    return left_2, top_2

def slot_3(left_3, top_3):
    left_3 = left_1+60
    top_3 = top_1
    return left_3, top_3

def slot_4(left_4, top_4):
    left_4 = left_1+90
    top_4 = top_1
    return left_4, top_4

def slot_5(left_5, top_5):
    left_5 = left_1+120
    top_5 = top_1
    return left_5, top_5

def slot_6(left_6, top_6):
    left_6 = left_1+150
    top_6 = top_1
    return left_6, top_6

def slot_7(left_7, top_7):
    left_7 = left_1+180
    top_7 = top_1
    return left_7, top_7

def slot_8(left_8, top_8):
    left_8 = left_1+210
    top_8 = top_1
    return left_8, top_8

def slot_9(left_9, top_9):
    left_9 = left_1+240
    top_9 = top_1 
    return left_9, top_9

def slot_10(left_10, top_10):
    left_10 = left_1+270
    top_10 = top_1 
    return left_10, top_10

def slot_11(left_11, top_11):
    left_11 = left_1
    top_11 = top_1 +25
    return left_11, top_11

def slot_12(left_12, top_12):
    left_12 = left_1+30
    top_12 = top_1 +25
    return left_12, top_12

def slot_13(left_13, top_13):
    left_13 = left_1+60
    top_13 = top_1 +25
    return left_13, top_13

def slot_14(left_14, top_14):
    left_14 = left_1+90
    top_14 = top_1 +25
    return left_14, top_14

def slot_15(left_15, top_15):
    left_15 = left_1+120
    top_15 = top_1 +25
    return left_15, top_15

def slot_16(left_16, top_16):
    left_16 = left_1+150
    top_16 = top_1 +25
    return left_16, top_16

def slot_17(left_17, top_17):
    left_17 = left_1+180
    top_17 = top_1 +25
    return left_17, top_17

def slot_18(left_18, top_18):
    left_18 = left_1+210
    top_18 = top_1 +25
    return left_18, top_18

def slot_19(left_19, top_19):
    left_19 = left_1+240
    top_19 = top_1 +25
    return left_19, top_19

def slot_20(left_20, top_20):
    left_20 = left_1+270
    top_20 = top_1 +25
    return left_20, top_20

left_1, top_1 = slot_1(0, 0)
left_2, top_2 = slot_2(0, 0)
left_3, top_3 = slot_3(0, 0)
left_4, top_4 = slot_4(0, 0)
left_5, top_5 = slot_5(0, 0)
left_6, top_6 = slot_6(0, 0)
left_7, top_7 = slot_7(0, 0)
left_8, top_8 = slot_8(0, 0)
left_9, top_9 = slot_9(0, 0)
left_10, top_10 = slot_10(0, 0)
left_11, top_11 = slot_11(0, 0)
left_12, top_12 = slot_12(0, 0)
left_13, top_13 = slot_13(0, 0)
left_14, top_14 = slot_14(0, 0)
left_15, top_15 = slot_15(0, 0)
left_16, top_16 = slot_16(0, 0)
left_17, top_17 = slot_17(0, 0)
left_18, top_18 = slot_18(0, 0)
left_19, top_19 = slot_19(0, 0)
left_20, top_20 = slot_20(0, 0)

def XP():
    if left_1 is not None and top_1 is not None:
        pyautogui.moveTo(left_1, top_1)



if __name__ == "__main__":
    sleep(1)
    print (1)
    sleep(1)
    print(2)
    XP()
    print(3)
    left_1, top_1 = slot_1(0, 0)
    left_2, top_2 = slot_2(0, 0)
    left_3, top_3 = slot_3(0, 0)
    left_4, top_4 = slot_4(0, 0)
    left_5, top_5 = slot_5(0, 0)
    left_6, top_6 = slot_6(0, 0)
    left_7, top_7 = slot_7(0, 0)
    left_8, top_8 = slot_8(0, 0)
    left_9, top_9 = slot_9(0, 0)
    left_10, top_10 = slot_10(0, 0)
    left_11, top_11 = slot_11(0, 0)
    left_12, top_12 = slot_12(0, 0)
    left_13, top_13 = slot_13(0, 0)
    left_14, top_14 = slot_14(0, 0)
    left_15, top_15 = slot_15(0, 0)
    left_16, top_16 = slot_16(0, 0)
    left_17, top_17 = slot_17(0, 0)
    left_18, top_18 = slot_18(0, 0)
    left_19, top_19 = slot_19(0, 0)
    left_20, top_20 = slot_20(0, 0)
    print("New position of slot 1:", left_1, top_1)
    print("New position of slot 2:", left_2, top_2)
    print("New position of slot 3:", left_3, top_3)
    print("New position of slot 4:", left_4, top_4)
    print("New position of slot 5:", left_5, top_5)
    print("New position of slot 6:", left_6, top_6)
    print("New position of slot 7:", left_7, top_7)
    print("New position of slot 8:", left_8, top_8)
    print("New position of slot 9:", left_9, top_9)
    print("New position of slot 10:", left_10, top_10)
    print("New position of slot 11:", left_11, top_11)
    print("New position of slot 12:", left_12, top_12)
    print("New position of slot 13:", left_13, top_13)
    print("New position of slot 14:", left_14, top_14)
    print("New position of slot 15:", left_15, top_15)
    print("New position of slot 16:", left_16, top_16)
    print("New position of slot 17:", left_17, top_17)
    print("New position of slot 18:", left_18, top_18)
    print("New position of slot 19:", left_19, top_19)
    print("New position of slot 20:", left_20, top_20)
