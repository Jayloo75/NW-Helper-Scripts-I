#  Run this script in 1920 x 1200 resolution and FOV 70
#  great page on using opencv to compare color ranges
#  https://github.com/tehzwen/WoWCV/blob/a25da9a539baf11e15f5428d478109a71459e76b/findTargetInWorld.py#L12

import pyautogui
import pydirectinput
import time
import random
import sys
import keyboard
import cv2
import time
import threading
import numpy as np
from PIL import ImageGrab
import pytesseract as tess
import win32api
# from classes.windows_class import Windows
from classes.windows_class import Windows
from classes.fishing_windows import FishingWindow


def main():
    """
    Main function for the program
    """
    print("main function Initiated")# Initiate windows classfrom classes.windows_class import Windows
    win_obj = Windows()
    fw_obj = FishingWindow(win_obj)

    print("get_region_full_window", fw_obj.get_region_full_window())

    # gather_obj = Gather()
    start_time = 0
    duration_time = 0
    cycler = True
    bot_stage = 0

# # Finds all Windows with the title "New World"
#     newWorldWindows = pyautogui.getWindowsWithTitle("New World")
#
#     # Find the Window titled exactly "New World" (typically the actual game)
#     for window in newWorldWindows:
#         if window.title == "New World":
#             newWorldWindow = window
#             break

    # Randomly will move right or left to keep from AFKing
    move_direction = ["a", "d"]

    # Select that Window
    # newWorldWindow.activate()
    # print("NW Window Location x=", newWorldWindow.left, " z=", newWorldWindow.top,
    #       " width=", newWorldWindow.width, " height", newWorldWindow.height, )
    # Move your mouse to the center of the game window
    # centerW = windows_obj.left + (windows_obj.width / 2)
    # centerH = windows_obj.top + (windows_obj.height / 2)
    # pyautogui.moveTo(centerW, centerH)
    #
    # time.sleep(random.randint(254, 652) / 1000)
    # pyautogui.click()

    #pause 3 seconds then move mouse a bit.
    #time.sleep(3)


    #aaaaaaaaaaaaaa.move(-1700, 0, relative=True)

    ##print("Moving Mouse")
    ##pydirectinput.move(-1700, 0, relative=True)
    #pyautogui.moveTo(600, 200, 3, pyautogui.easeInOutQuad)
    #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))

    # Making tuple with data from the window for later use
    # Point(x=1049, y=174) upper left
    # Point(x=1438, y=1004)  lower right
    #x1 = 1049
    #x2 = 1438
    #y1 = 174
    #y2 = 1004
    #regionFullWindow = (newWorldWindow.left, newWorldWindow.top, newWorldWindow.width, newWorldWindow.height)
    #region = (x1, y1, x2 - x1, y2 - y1)

    region_middle_third = fw_obj.get_region_middle_third()
    print("region_middle_third", region_middle_third)
    fish_caught_level_bubble_region = fw_obj.get_fish_caught_level_bubble_region()

    #Point(x=1861, y=19)
    #Point(x=2551, y=280)
    xx1 = 1861
    xx2 = 2551
    yy1 = 19
    yy2 = 280
    region_still_playing = (xx1, yy1, xx2 - xx1, yy2 - yy1)

    # Making tuple with data from the window for later use
    # Point(x=1368, y=923)
    # Point(x=1668, y=1109)
    x1 = 1368
    x2 = 1668
    y1 = 923
    y2 = 1109
    # regionFullWindow = (newWorldWindow.left, newWorldWindow.top, newWorldWindow.width, newWorldWindow.height)
    regionHoldCast = (x1, y1, x2 - x1, y2 - y1)



    mouse_click_down = 0

    start_time = time.time()
    last_time = time.time()
    step_time = time.time()

    # gather counter
    gatherCounter = 0

    switch_case = 0;
    reeling_switch = 0
    casting_switch = 0
    # mouse_down_max = 3000

    success_caught_fish_global = 0

    while True:
        while cycler:
            # Default/Initial state of while loop
            #  Deals with the "are you still playing" pop up
            #  Also a good spot to reset any variables that may have run away
            if bot_stage == 0:
                # Are you still Playing - how to deal with this - set a trigger then at most convienient time move character
                if pyautogui.locateOnScreen("imgs/still_playing.png", grayscale=True, confidence=.85, region=region_still_playing) is not None:
                    print("Are You Still Playing?")
                    # Move forward then back for a sec
                    key = move_direction[random.randint(0, 1)]
                    pyautogui.keyDown(key)
                    time.sleep(random.randint(70, 170) / 1000)
                    pyautogui.keyUp(key)
                    bot_stage = 69
                else:
                    bot_stage = 101

            # FInd fishing controls on screen and start the party
            if bot_stage == 101:
                # Clean up all variables (reset them) and start the casting
                if pyautogui.locateOnScreen("imgs/cast_f3.png", grayscale=True, confidence=.85, region=region_middle_third) is not None:
                    start_fishing_cycle_timer = time.time()
                    if random.randint(1, 5) == 5:
                        key = move_direction[random.randint(0, 1)]
                        pyautogui.keyDown(key)
                        time.sleep(.1)
                        pyautogui.keyUp(key)
                    bot_stage = 1

            # Simple announcement that fishing controls were found and to initiate the cast
            if bot_stage == 1:
                print("Fishing Controls Recognized.")
                print("Fishing Bot Initiated.  Let's go!")
                bot_stage = 2

            # Cast the line
            if bot_stage == 2:
                if casting_switch == 0:
                    # print("Casting switch = " + str(casting_switch))
                    ##random_cast_hold_delay = random.randint(2568, 3150) / 1000
                    random_cast_hold_delay = random.randint(1168, 1450) / 1000
                    # random_casting_delay = random.randint(1792, 1979) / 1000  # $Max Distance
                    random_casting_delay = random.randint(250, 300) / 1000    # shorty distance
                    # Like it says, casting
                    time.sleep(random_cast_hold_delay)
                    print("Start Casting - " + str(random_casting_delay) + " seconds")
                    pyautogui.mouseDown()
                    time.sleep(random_casting_delay)
                    pyautogui.mouseUp()
                    print("Finish Casting")
                    casting_switch = 1
                    bot_stage = 3

            # Detect the Waiting icon for fishing -= watching the bobber
            if bot_stage == 3:
                if pyautogui.locateOnScreen("imgs/fishing_casted.png", grayscale=True, confidence=.85, region=region_middle_third) is not None:
                    print("Don't take your eye off the bobber...")
                    bot_stage = 4

            # Detect the HOOKED icon
            if bot_stage == 4:
                if pyautogui.locateOnScreen("imgs/fishing_hooked1.png", grayscale=True, confidence=.85,
                                            region=region_middle_third) is not None:
                    print("You hooked a fish.")
                    bot_stage = 5

            # initial mousedown to begin catching the fish
            if bot_stage == 5:
                print("Step #1 - Hooked em")
                gatherCounter = gatherCounter + 1

                #print("Fish Counter: " + str(gatherCounter))
                random_mouse_delay = random.randint(175, 250) / 1000

                #print(random_mouse_delay)
                time.sleep(random_mouse_delay)

                mouse_click_down = 1
                pyautogui.mouseDown();

                casting_switch = 0  # reset casting switch so we can cast again when able
                reeling_switch = 1
                bot_stage = 6

            #  Reel in the fish while checking for the image that you caught the fish
            if bot_stage == 6:

                #print ("fishing cycle timer - " + str(time.time()-start_fishing_cycle_timer))
                if time.time()-start_fishing_cycle_timer > 26:

                    if time.time() - start_fishing_cycle_timer > 180:
                        print("WARMING #1 - Cycle timer too long " + str(time.time() - start_fishing_cycle_timer) + " this session!")
                    if time.time() - step_time > 8:
                        print("WARNING #2 - Step timer too long " + str(time.time() - step_time) + " Start this shit over!")
                        bot_stage = 69

                    # if pyautogui.locateOnScreen("imgs/fish_caught_level_bubble.png", grayscale=False, confidence=.95,
                    #                             region=fish_caught_level_bubble_region) is not None or time.time() - start_fishing_cycle_timer > 180 or time.time() - step_time > 8:

                    if pyautogui.locateOnScreen("imgs/fish_caught_level_bubble.png", grayscale=False, confidence=.95, region=fish_caught_level_bubble_region) is not None:
                        print("Fish Caught in " + str(round(time.time()-start_fishing_cycle_timer, 1)) +" seconds!")
                        print("You've caught " + str(gatherCounter) +" this session!")
                        #print("Fish Caught - Nice work!   ----   Let's do it again shall we.")
                        print("=============================================================")
                        bot_stage = 69

                if reeling_switch == 0:  # Release mouse button and release tension
                    if mouse_click_down == 1:
                        print("Mouse up - relax a bit")
                        random_catching_delay = random.randint(1, 99) / 1000
                        time.sleep(random_catching_delay)  ################################################################
                        pyautogui.mouseUp()
                        mouse_click_down = 0
                    elif pyautogui.locateOnScreen("imgs/fishing_hooked_mousedown1.png", grayscale=False, confidence=.65,
                                                region=region_middle_third) is not None:
                        print("mousedown1 timer = " + str(round(time.time()-step_time, 1)) +" seconds!")
                        step_time = time.time()
                        reeling_switch = 1

                elif reeling_switch == 1:  # Press mouse down and reel in the fish
                    if mouse_click_down == 0:
                        print("Mouse down - lets reel en in bro")
                        random_catching_fastdelay = random.randint(1, 58) / 1000
                        time.sleep(random_catching_fastdelay)  ################################################################
                        pyautogui.mouseDown();
                        mouse_click_down = 1
                    elif pyautogui.locateOnScreen("imgs/fishing_hooked_mouseup1.png", grayscale=False, confidence=.65,
                                            region=region_middle_third) is not None:
                        print("mouseup1 timer = " + str(round(time.time()-step_time, 1)) +" seconds!")
                        step_time = time.time()
                        reeling_switch = 0


            if bot_stage == 69:
                if mouse_click_down == 1:
                    print("Found that mouse_click_down == 1 so sending mouseuo command.")
                    pyautogui.mouseUp()
                    casting_switch = 0
                bot_stage = 0

            if keyboard.is_pressed('f1'):
                print("\nyou pressed F1, so pausing...")
                cycler = False
                time.sleep(1)

        if keyboard.is_pressed('f1'):
            print("\nyou pressed F1, so resuming...")
            cycler = True


            ##  Check out this fishing bot on github  https://github.com/GlacianNex/new_world_fishing_bot/blob/main/src/fishing_bot.py

# Runs the main function
if __name__ == '__main__':
    main()
