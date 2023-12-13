import time
import threading

def your_function():
    # Put the code you want to run every 10 minutes here
    print("This code runs every 10 minutes.")

def run_thread():
    while True:
        your_function()
        time.sleep(6)  # 600 seconds = 10 minutes

# Create and start the thread
thread = threading.Thread(target=run_thread)
thread.start()