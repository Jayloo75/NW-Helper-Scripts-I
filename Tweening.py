import pyautogui
import pydirectinput
import pytweening
import time
import win32api
import win32con
import random
import sys
import keyboard
from math import sqrt
import numpy as np


#     # Finds all Windows with the title "New World"
# newWorldWindows = pyautogui.getWindowsWithTitle("New World")
#
# # Find the Window titled exactly "New World" (typically the actual game)
# for window in newWorldWindows:
#     if window.title == "New World":
#         newWorldWindow = window
#         break

# # Randomly will move right or left to keep from AFKing
# moveDirection = ["a", "d"]
#
# # Select that Window
# newWorldWindow.activate()
# print("NW Window Location x=", newWorldWindow.left, " z=", newWorldWindow.top,
#       " width=", newWorldWindow.width, " height", newWorldWindow.height, )
# # Move your mouse to the center of the game window
# centerW = newWorldWindow.left + (newWorldWindow.width / 2)
# centerH = newWorldWindow.top + (newWorldWindow.height / 2)
# pyautogui.moveTo(centerW, centerH)
#
# time.sleep(random.randint(254, 652) / 1000)
# pyautogui.click()

def move_smooth(x2, y2, t):
    x_start, y_start = win32api.GetCursorPos()
    x_start = -2009
    y_start = 1208
    print ("starting location = ", x_start, ", ", y_start)

    point_counter = 0
    points = pytweening.getLine(x_start, y_start, x2, y2)

    # points = np.array(points)
    # # points = np.delete(points, np.arange(0, points.size, 3))    #
    # points - np.delete(points, list(range(0, points.shape[0], 2)), axis=0)

    num_of_points = len(points)
    hypotenuse_length = sqrt((x2 - x_start)**2 + (y2 - y_start)**2)

    print("num_of_points = ", num_of_points)
    print("hypotenuse_length = ", hypotenuse_length)

    print(points)

    # time_to_dest = num_of_points * 0.010;
    time_to_dest = num_of_points * 0.01646;
    if t > time_to_dest:
        print("Need to speed it up", time_to_dest)
    else:
        print("Need to slow it down", time_to_dest)

    start_time = time.time()
    for startPoint in points:

        point_counter = point_counter + 1
        #if point_counter % 2 == 1:
        #x_dest = x_start + startPoint[0]
        #y_dest = y_start + startPoint[1]
        print("Point", point_counter , "/", num_of_points, "  x,y: ", startPoint[0], ",", startPoint[1], "timer:",  round(time.time() - start_time, 6))
        #win32api.mouse_event(1, x_dest, y_dest, 0, 0)
        win32api.SetCursorPos([startPoint[0], startPoint[1]])
        #time.sleep(0.010)
        # Windows installation, the smallest interval you may delay is 10 - 13 milliseconds

        if keyboard.is_pressed('Esc'):
            print("you pressed Esc, so exiting...")
            sys.exit(0)


move_smooth(-1747, 883, 2)
