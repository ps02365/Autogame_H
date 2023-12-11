import win32gui
import time
import pydirectinput
import pyautogui

# pyautogui.FAILSAFE = False
# pydirectinput.FAILSAFE = False

# def focus_dream_ace():
#     hwnd = win32gui.FindWindow(None, "DreamACE")
#     if not hwnd:
#         raise Exception("Not found DreamACE window")
#     win32gui.SetForegroundWindow(hwnd)

# def hold():    
#     pydirectinput.press("c")
#     time.sleep(0.5)
#     pydirectinput.keyDown("s")
#     time.sleep(0.05)
#     pydirectinput.keyDown("a")
#     time.sleep(0.05)
#     pyautogui.mouseDown(button='right')
#     time.sleep(0.05)
#     pyautogui.moveTo((1920/8)*5,540)    
#     time.sleep(0.05)
#     #
# def release():  
#     pydirectinput.keyUp("s")
#     time.sleep(0.05)
#     pydirectinput.keyUp("a")
#     time.sleep(0.05)
#     pyautogui.mouseUp(button='right')
#     time.sleep(0.05)

# if __name__ == "__main__":
#     focus_dream_ace()
#     time.sleep(0.5)
#     hold()    
#     for x in range(6): 
#         if x % 2 == 0:    
#             release()
#             hold()
#         time.sleep(5)
#     release()




import tkinter as tk

def button1_click():
    print("Button 1 clicked")

def button2_click():
    print("Button 2 clicked")

# Create the main window
root = tk.Tk()
root.title("Two Buttons Example")

# Create Button 1
button1 = tk.Button(root, text="Button 1", command=button1_click)
button1.pack(pady=10)

# Create Button 2
button2 = tk.Button(root, text="Button 2", command=button2_click)
button2.pack(pady=10)

# Start the GUI event loop
root.mainloop()