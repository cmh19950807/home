import win32api
import time
import pyautogui

checktime = 0
cnt = 0
while True:
    # print(win32api.GetKeyState(0x02))
    if win32api.GetKeyState(0x02) < -10:
        break

    if (checktime % 290 == 0):
        pyautogui.moveRel(0, 100, 0.1)
        time.sleep(0.1)
        pyautogui.moveRel(0, -100, 0.1)
        checktime = 0
        cnt = cnt + 1
        print('5min over', cnt)
    checktime = checktime+1
    time.sleep(0.1)
