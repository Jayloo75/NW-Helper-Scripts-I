import sys
import random
import time
import pyautogui
import pydirectinput
from classes.windows_class import Windows

# from classes.Actions import holdclick,releaseclick

pydirectinput.PAUSE = 0

def drag(x1, y1, x2, y2, duration, rate):
    steps = int(duration / rate)
    dx = (x2 - x1) / steps
    dy = (y2 - y1) / steps
    startTime = time.time()
    lagCount = 0
    for i in range(steps):
        pydirectinput.moveTo(int(x1 + i * dx), int(y1 + i * dy))
        try:
            time.sleep(rate * (i + 1) + startTime - time.time())
        except ValueError:
            lagCount += 1
    print(steps, lagCount)

def pyMove(x, y, duration, rate):
    steps = int(duration / rate)
    dx = (x) / steps
    dy = (y) / steps
    startTime = time.time()
    lagCount = 0
    for i in range(steps):
        # pydirectinput.move(int(x + i * dx), int(y + i * dy))
        pydirectinput.move(int(dx), None)

        print(int(dx))
        try:
            time.sleep(rate * (i + 1) + startTime - time.time())
        except ValueError:
            lagCount += 1
    print(steps, lagCount)




def get_auctioneer_scroll_mid():
    x1 = 2244
    y1 = 836
    x2 = 2257
    y2 = 1048
    x_rand = random.randint(x1, x2)
    y_rand = random.randint(y1, y2)
    return [x_rand, y_rand]


print("1", pyautogui.position())
windows_obj = Windows()
print("2", pyautogui.position())
# newWorldWindow = windows_obj.newWorldWindow
time.sleep(2.5)
print("3", pyautogui.position())
x, y = pyautogui.position()
time.sleep(.5)
print("4", pyautogui.position())
pydirectinput.click()
# sys.exit()

print("5", pyautogui.position())
# auctioneer_scroll_mid = get_auctioneer_scroll_mid()
# print(auctioneer_scroll_mid)
time.sleep(1.5)
print("Move thur")
# pydirectinput.move(828, None)
# pyMove(100, 5, 2, 0.1)
# pydirectinput.move(220, None)
# drag(x1, y1, x2, y2, duration, rate):

print("6", pyautogui.position())
pydirectinput.move(100, None)
# drag(x, y, 1400, 694, 2, 0.01)
# drag(1168, 657, 1400, 694, 2, 0.01)
time.sleep(.5)

print("7", pyautogui.position())
# drag(959, 621, 1052, 621, 5, 0.01)
# print(pyautogui.position())
# pydirectinput.click(auctioneer_scroll_mid[0], auctioneer_scroll_mid[1])

# pydirectinput.leftClick(auctioneer_scroll_mid[0], auctioneer_scroll_mid[1],)
# time.sleep(1)
# pydirectinput.leftClick(auctioneer_scroll_mid[0], auctioneer_scroll_mid[1],)





# # pydirectinput.leftClick(1900, 536,)
# # time.sleep(1)
# # pydirectinput.leftClick(1900, 536,)
# # time.sleep(1)
# # pydirectinput.press('esc')
# #
# # time.sleep(1)
# pydirectinput.mouseDown(2160, 536, 'left')
#
#
# time.sleep(1)
# # pywinauto.mouse.press(button='left', coords=(2160, 536))
#
# print("move it")
# time.sleep(1.5)
# drag(2160, 536, 2163, 870, 1, 0.01)
# time.sleep(1)
#
#
# pydirectinput.mouseUp(2163, 870, 'left')
# # pywinauto.mouse.release(button='left', coords=(2163, 870))




