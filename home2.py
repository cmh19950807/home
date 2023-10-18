import win32api
import time
import pyautogui

checktime = 0
cnt = 0
while True:
    # print(win32api.GetKeyState(0x02))
    pyautogui.moveRel(0, 100, 0.1)
    time.sleep(250)
    cnt = cnt+1
    print('5min time over', cnt)
    pyautogui.moveRel(0, -100, 0.1)
    time.sleep(250)
    cnt = cnt+1
    print('5min time over', cnt)
