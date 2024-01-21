import pyautogui
from time import sleep
import pygetwindow as gw
import os


def start_game():
    gw.getWindowsWithTitle('DreamACE')[0].activate()
    sleep(1)
    
    find_image_on_screen()

def find_image_on_screen(template_path):
    try:
        # Lấy đường dẫn tuyệt đối của template
        template_path_absolute = os.path.abspath(template_path)

        # Tìm vị trí xuất hiện của hình ảnh trên màn hình
        location = pyautogui.locateOnScreen(template_path_absolute)

        if location is not None:
            return True, location
        else:
            return False, None
    except Exception as e:
        print(f"Lỗi: {e}")
        return False, None

# Đường dẫn đến hình ảnh template cần tìm trên màn hình
template_path = 'D:/Python/Project/out_of_ammunition.png'

# Kiểm tra xem hình ảnh có xuất hiện trên màn hình không
found, location = find_image_on_screen(template_path)

if found:
    print(f"Hình ảnh được tìm thấy tại vị trí {location}")
else:
    print("Hình ảnh không xuất hiện trên màn hình")

start_game()

# import os
# current_directory = os.getcwd()
# print(f"Thư mục hiện tại: {current_directory}")