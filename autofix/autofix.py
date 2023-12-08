import pyautogui
import win32gui
from time import sleep
import keyboard
from enum import Enum
import os

class FixType(Enum):
    PREFIX = 'prefix'
    SUFFIX = 'suffix'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class AvailableFix(Enum):
    SATURN = 'saturn'
    FORAS = 'foras'
    ULTRA = 'ultra'
    ORIGIN = 'origin'
    # OSE = 'ose'

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class AutoFix():
    def __init__(self, fix_type = FixType.PREFIX.value, fix_name = None) -> None:
        if fix_name is None:
            raise Exception("Please fill fix name")
        self.fix_name = fix_name
        self.fix_type = fix_type
        if fix_type == FixType.PREFIX.value:
            self.fix_img_path = f'prefix_imgs\{self.fix_name}.png'
        elif fix_type == FixType.SUFFIX.value:
            self.fix_img_path = f'suffix_imgs\{self.fix_name}.png'
        else:
            raise Exception("No fix type available")


def find_window_and_active():
    hwnd = win32gui.FindWindow(None, "DreamACE")
    if not hwnd:
        raise Exception("Not found DreamACE window")
    win32gui.SetForegroundWindow(hwnd)


def add_weapon():
    sleep(0.05)
    pyautogui.doubleClick(920, 908, button="left")
    sleep(0.05)


def confirm_update():
    sleep(0.05)
    pyautogui.leftClick(1270, 687)
    sleep(2)
    pyautogui.leftClick(1270, 687)
    sleep(0.1)
    pyautogui.moveTo(920, 908)
    sleep(0.1)


def add_fix_removal(should_add_fix=False):
    add_weapon()
    sleep(0.1)
    pyautogui.doubleClick(863, 908, button="left")
    sleep(0.1)
    confirm_update()
    # if should_add_fix:
    #     add_weapon()
    #     add_fix()


def add_fix():
    add_weapon()
    sleep(0.1)
    pyautogui.doubleClick(892, 908, button="left")
    sleep(0.1)
    confirm_update()


def run(fix_type=FixType.PREFIX.value, fix_name = None): 
    find_window_and_active()
    autofix = AutoFix(fix_type=fix_type, fix_name=fix_name)
    sleep(0.1)
    pyautogui.moveTo(920, 908)

    sleep(0.1)

    if pyautogui.locateOnScreen(autofix.fix_img_path, confidence=0.9):
        print(f"Already has {autofix.fix_name} {autofix.fix_type}")
        exit()

    while True:
        if keyboard.is_pressed('q'):
            print('Q Pressed')
            exit()
        add_fix()
        sleep(0.1)
        if pyautogui.locateOnScreen(autofix.fix_img_path, confidence=0.9):
            print("Success.")
            exit()
        add_fix_removal()

class ConsoleUI():
    current_option_to_select = 'fix'
    selected_fix = 0
    confirm_fix = None
    selected_fix_type = 0
    confirm_fix_type = None

    menu_title = ""
    selected_field_name_for_menu = "selected_fix_type"
    menu_list_option = []

    def __init__(self):
        self.menu_title = "Select fix type"
        self.selected_field_name_for_menu = "selected_fix_type"
        self.menu_list_option = FixType.list()
        self.show_menu()
        keyboard.add_hotkey('up', self.up)
        keyboard.add_hotkey('down', self.down)
        keyboard.add_hotkey('enter', self.set_confirm_fix_type)    
        while self.confirm_fix_type is None:
            pass
        #---------------------------------------------------------
        self.menu_title = "Select fix"
        self.selected_field_name_for_menu = "selected_fix"
        self.menu_list_option = AvailableFix.list()
        self.show_menu()
        keyboard.add_hotkey('up', self.up)
        keyboard.add_hotkey('down', self.down)
        keyboard.add_hotkey('enter', self.set_confirm_fix)

        while self.confirm_fix is None:
            pass

        print(f"{self.confirm_fix_type}")
        print(f"{self.confirm_fix}")
    
    def set_confirm_fix(self):
        self.confirm_fix = AvailableFix.list()[self.selected_fix]

    def set_confirm_fix_type(self):
        self.confirm_fix_type = FixType.list()[self.selected_fix_type]

    def show_menu(self):
        field_value = getattr(self, self.selected_field_name_for_menu) 
        print(self.menu_title)
        for idx, i in enumerate(self.menu_list_option):
            print("{1} {0} {2}".format(i, ">" if field_value == idx else " ", "<" if field_value == idx else " "))

    def up(self):
        field_value = getattr(self, self.selected_field_name_for_menu)
        if field_value == 0:
            return
        setattr(self, self.selected_field_name_for_menu, field_value - 1)
        os.system('cls')
        self.show_menu()

    def down(self):
        field_value = getattr(self, self.selected_field_name_for_menu)
        if field_value == len(self.menu_list_option) - 1:
            return
        setattr(self, self.selected_field_name_for_menu, field_value + 1)
        os.system('cls')
        self.show_menu()
    pass


console_ui = ConsoleUI()
run(fix_type=console_ui.confirm_fix_type,fix_name=console_ui.confirm_fix)
        
    

