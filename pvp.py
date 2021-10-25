# encoding: UTF-8
# refer: https://nga.178.com/read.php?tid=11838545
# python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyautogui Pillow
# python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymouse PyUserinput pypiwin32

import re
import pyautogui
import time
from pymouse import PyMouse
import win32gui
from winguiauto import findTopWindow
import os

global LOGFILE, encoding, m, zoom
pyautogui.FAILSAFE = False
LOGFILE = "C:\\Program Files (x86)\\Hearthstone\\Logs\\Power.log"
encoding = "UTF-8"
zoom = 1    # Windows system zoom
m = PyMouse()


def findHS():
    hwnd = findTopWindow("炉石传说")
    rect = win32gui.GetWindowPlacement(hwnd)[-1]
    return rect


def get_xy(zoom = zoom):
    for i in range(1000):
        x, y = m.position()
        rect = findHS()
        print(((x-rect[0])/zoom, (y-rect[1])/zoom))
        time.sleep(0.1)
    return x, y

def movClick(x, y, t=0.7, zoom = zoom):
    #pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)
    #time.sleep(0.3)
    #pyautogui.click()
    #time.sleep(0.233)
    rect = findHS()
    m.click(int(x * zoom + rect[0]),int(y * zoom + rect[1]))
    time.sleep(t)


def gaming(flag=0):
    flagGameover = 0
    flagTimesleep = 0
    with open(LOGFILE, 'r', encoding=encoding) as log:
        while log.readline():
            pass
        while True:
            line = log.readline()
            if line:
                print(line)
                flagTimesleep = 0
                if re.findall(r"tag=STEP value=MAIN_ACTION", line):
                    time.sleep(10)    # delay
                    pyautogui.press('esc')
                    time.sleep(1)
                    movClick(278, 171)
                    movClick(514, 242)
                    movClick(514, 242)
                    logLine = log.readline()
                    while logLine:
                        if re.findall(r"FINAL_GAMEOVER", logLine):
                            flagGameover += 1
                        logLine = log.readline()
                    continue
                elif re.findall(r"FINAL_GAMEOVER", line):
                    time.sleep(5)
                    logLine = log.readline()
                    while logLine:
                        if re.findall(r"FINAL_GAMEOVER", logLine):
                            flagGameover += 1
                        logLine = log.readline()
                    flagGameover += 1
            else:
                time.sleep(1)
                flagTimesleep += 1
                print(flagTimesleep)
            if flagGameover >= 4:
                return
            if flagTimesleep >= 123:                
                movClick(289, 151)
                movClick(289, 151)
                movClick(157, 199)
                movClick(157, 199)
                movClick(192, 354)
                movClick(192, 354)
                movClick(382, 363)
                movClick(382, 363)
                movClick(427, 204)
                movClick(427, 204)
                loc = findHS()
                pyautogui.screenshot(f"./hs/pvp/{time.time()}.png",region=(loc[0],loc[1],548*zoom,439*zoom))
                movClick(284, 243)
                movClick(284, 243)
                return
                    


if __name__ == '__main__':
    print(time.time())
    try:
        os.mkdir("./hs")
        os.mkdir("./hs/pvp")
    except:
        pass
    while True:
        try:
            movClick(443, 368)
            movClick(443, 368)
            movClick(443, 368)
            movClick(443, 368)
            gaming()
            movClick(514, 242)
            movClick(514, 242)
            movClick(514, 242)
            movClick(514, 242)
            print("done")
        except FileNotFoundError:
            time.sleep(0.233)

    #get_xy()