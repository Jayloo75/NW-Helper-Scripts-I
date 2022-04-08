import pyautogui
import pydirectinput
import time
import random
import keyboard
import sys
from PIL import ImageGrab
from classes.windows_class import Windows
from classes.gather import Gather


# Save a snapshot of the current active weapon 1 slot to know when gathering is complete
def save_weapon_1_image(windows_obj):
    # region_x = round(windows_obj.left + windows_obj.width - 58)
    # region_y = round(windows_obj.top + windows_obj.height - 223)
    x1 = windows_obj.left + 1702
    y1 = windows_obj.top + 999
    x2 = x1 + 165
    y2 = y1 + 72
    ss_region = (x1, y1, x2, y2)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save("imgs/save_weapon_1_image.jpg")


def main():
    """
    Main function for the program
    """
    print("main function Initiated")# Initiate windows class
    windows_obj = Windows()

    # print("region_full_window", Windows.region_full_window)
    # print("region_gather", Windows.region_gather)
    gather_obj = Gather()
    start_time = 0
    duration_time = 0
    cycler = True
    bot_stage = 0

    while 1:
        while cycler:
            # Initial default state - reset any variables here
            if bot_stage == 0:
                print(bot_stage, " -------------- Script Restarting -----------------")
                bot_stage = 1

            # Status Message
            elif bot_stage == 1:
                print(bot_stage, " - Searching for E")
                bot_stage = 2

            # Find the Interactable "E"
            elif bot_stage == 2:
                # Find that image on screen, in that region, with a confidence of 65%
                #if pyautogui.locateOnScreen("imgs/e0.png", grayscale=True, confidence=.65, region=region) is not None:
                if pyautogui.locateOnScreen("imgs/e1.png", grayscale=True, confidence=.85,
                                            region=windows_obj.region_gather) is not None:
                    print(bot_stage, " - I found an interactable E Object")
                    start_time = time.time()
                    bot_stage = 3

            # let's check some shit
            elif bot_stage == 3:
                print(bot_stage, " - Save initial state of weapon #1")
                save_weapon_1_image(windows_obj)  # save weapon 1 initial state to file
                bot_stage = 4

            # let's gather some shit
            elif bot_stage == 4:
                print(bot_stage, " - Pressing 'E' to start gathering")
                pyautogui.press('e')
                Gather.incrementGatherCounter(gather_obj)
                #Gather.gatherCounter = Gather.gatherCounter + 1
                #isGatheringNode = 1

                time.sleep(random.randint(250, 500) / 1000)
                # print(windows_obj.region_weapon_1)
                # print("3 - Goto line 4")
                bot_stage = 5

            # # Look for weapon pixel to know that you are done gathering
            # elif bot_stage == 44:
            #     # print("4 - Looking for weapon 1 icon")
            #     # print(windows_obj.region_weapon_icon_1)
            #     if pyautogui.locateOnScreen("imgs/weapon-1.png", grayscale=True, confidence=.85,
            #                                 region=windows_obj.region_weapon_icon_1) is not None:
            #         gathering_message = "Chopping with a wood axe"
            #         bot_stage = 5

            # Status Message
            elif bot_stage == 5:
                print(bot_stage, " - Looking for weapon 1 initial status")
                bot_stage = 6

            # Look for weapon pixel to know that you are done gathering
            elif bot_stage == 6:
                # print(bot_stage, " - Looking for weapon 1 icon")
                # print(windows_obj.region_weapon_1)
                if pyautogui.locateOnScreen("imgs/save_weapon_1_image.jpg", grayscale=False, confidence=.85,
                                            region=windows_obj.region_weapon_1) is not None:
                    # gathering_message = "Chopping with a wood axe"
                    print(bot_stage, " - found clean weapon icon")
                    bot_stage = 8







            # # Are we actually gathering some shit and if yes, what
            # elif bot_stage == 55:
            #     # if pyautogui.locateOnScreen("imgs/gather-lumbering-1.png", grayscale=True, confidence=.85,
            #     #                             region=windows_obj.region_tool) is not None:
            #     #     gathering_message = "Chopping with a wood axe"
            #     #     print("4 - Gathering Message - ", gathering_message)
            #     #     bot_stage = 6
            #     # elif pyautogui.locateOnScreen("imgs/gather-mining-1.png", grayscale=True, confidence=.85,
            #     #                               region=windows_obj.region_tool) is not None:
            #     #     gathering_message = "Mining with an pick axe"
            #     #     print("4 - Gathering Message - ", gathering_message)
            #     #     bot_stage = 6
            #     # elif pyautogui.locateOnScreen("imgs/gather-harvesting-1.png", grayscale=True, confidence=.85,
            #     #                               region=windows_obj.region_tool) is not None:
            #     #     gathering_message = "Harvesting with a sickle"
            #     #     print("4 - Gathering Message - ", gathering_message)
            #     #     bot_stage = 6
            #     # else:
            #     #     # Didn't actually start gathering anything so start over
            #     #     print("4 - Gathering Message - Dosen't look like I am gathering anything so goto 0")
            #     #     random_casting_delay = random.randint(10, 20) / 1000  # shorty distance
            #     #     time.sleep(random_casting_delay)
            #     bot_stage = 8

            # # are we done gathering
            # elif bot_stage == 6:
            #     #random_casting_delay = random.randint(10, 69) / 1000  # shorty distance
            #     #time.sleep(random_casting_delay)
            #     bot_stage = 7


            # are we done gathering
            elif bot_stage == 7:
                if pyautogui.locateOnScreen("imgs/gather-completed-1.png", grayscale=False, confidence=.95, region=windows_obj.region_tool) is not None:
                    print("7 - Gathering Completed")
                    duration_time = time.time() - start_time
                    print("(", gather_obj.getGatherCounter(), ") cycle gathering -", gathering_message , "in", round(duration_time,1), "seconds")
                    bot_stage = 8

            # Run to next spot
            elif bot_stage == 8:
                print("8 - Gathering Completed - No RUN")

                #     time.sleep(random_casting_delay)
                key = '='
                #print("pressing =")
                time.sleep(random.randint(450, 700) / 1000)
                pyautogui.press(key)
                bot_stage = 0

                # time.sleep(0.5)

            #print(pyautogui.locateOnScreen("imgs/gather-completed-1.png", grayscale=True, confidence=.85, region=Windows.region_tool))
            #temp = 5.9 * random.random()
            #currentFoward += temp
            #time.sleep(temp)

            # Do I got to explain?
            #pyautogui.press(autowalkKey)

            if keyboard.is_pressed('f1'):
                print("\nyou pressed F1, so pausing...")
                cycler = False
                time.sleep(1)
        if keyboard.is_pressed('f1'):
            print("\nyou pressed F1, so resuming...")
            cycler = True


# Runs the main function
if __name__ == '__main__':
    main()
