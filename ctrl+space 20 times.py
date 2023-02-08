import pyautogui
import time
import keyboard

times_pressed = 0

# Flag variables to check if 5, 10, 15, and 20 presses have been reached
pressed5 = False
pressed10 = False
pressed15 = False
pressed20 = False

time.sleep(2)
while times_pressed < 20:
    pyautogui.hotkey('space', 'right_ctrl')
    time.sleep(0.2)
    times_pressed += 1
    if times_pressed == 5:
        pressed5 = True
        print("Space and right control have been pressed 5 times.")
    if times_pressed == 10:
        pressed10 = True
        print("Space and right control have been pressed 10 times.")
    if times_pressed == 15:
        pressed15 = True
        print("Space and right control have been pressed 15 times.")
    if times_pressed == 20:
        pressed20 = True
        print("Space and right control have been pressed 20 times.")
print("Space and right control have been pressed", times_pressed, "times")