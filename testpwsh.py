import os
import pyautogui
import time
##C:\Windows\System32\WindowsPowerShell\v1.0

os.startfile(r'""C:\Windows\System32\WindowsPowerShell\v1.0\powershell""')
time.sleep(0.5)
pyautogui.write('shutdown /s')
pyautogui.press('enter')