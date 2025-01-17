# pip install pyautogui
import pyautogui
import time
import random

screen_width, screen_height = pyautogui.size()
print("width",screen_width, "height", screen_height)
while True:
    seconds =random.randint(1,3)
    print(f"sleep for (seconds) seconds")
    time.sleep(seconds)
    x_rand= random.randint(0,screen_width)
    y_rand=random.randint(0,screen_height)
    pyautogui.moveTo(x_rand,y_rand, duration=1)