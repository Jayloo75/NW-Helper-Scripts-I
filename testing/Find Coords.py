import pyautogui
import time
from classes.windows_class import Windows
import random

windows_obj = Windows()
win = windows_obj.newWorldWindow


coords_type = 'rel'  # rel or abs



# print(win.left)
# print(win.top)


while True:
    if coords_type == 'abs':
        print('ABS' + pyautogui.position())
    else:
        x, y = pyautogui.position()
        print('REL' , x-win.left, y-win.top )

    time.sleep(0.15)

# Home
#Left Point(x=1068, y=769)
#Right Point(x=1390, y=783)
#Top Point(x=1229, y=602)
#Bottom Point(x=1268, y=1005)
#top left Point(959, 525)
#bot Right 1390, 1005



# def get_auctioneer_scroll_mid():
#     x1 = 2244
#     y1 = 836
#     x2 = 2257
#     y2 = 1208
#     x_rand = random.randint(x1, x2)
#     y_rand = random.randint(y1, y2)
#     return [x_rand, y_rand]
#
# auctioneer_scroll_mid = get_auctioneer_scroll_mid()
#
# print(auctioneer_scroll_mid)
#
# pydirectinput.leftClick(auctioneer_scroll_mid[0]-200, auctioneer_scroll_mid[1])
