import pyautogui
import pydirectinput
import time
import random
import keyboard
import sys
from classes.windows_class import Windows
from classes.gather import Gather



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
                print("0 -------------- Starting -----------------")
                bot_stage = 1

            # Find the Interactable "E"
            elif bot_stage == 1:
                # Find that image on screen, in that region, with a confidence of 65%
                #if pyautogui.locateOnScreen("imgs/e0.png", grayscale=True, confidence=.65, region=region) is not None:
                if pyautogui.locateOnScreen("imgs/e1.png", grayscale=True, confidence=.85,
                                            region=windows_obj.region_gather) is not None:
                    print("1 - I found an interactable Object")
                    start_time = time.time()
                    bot_stage = 2

            # let's check some shit
            elif bot_stage == 2:
                bot_stage = 3

            # let's gather some shit
            elif bot_stage == 3:
                print("3 - Pressing 'E'")
                pyautogui.press('e')
                Gather.incrementGatherCounter(gather_obj)
                #Gather.gatherCounter = Gather.gatherCounter + 1
                #isGatheringNode = 1

                time.sleep(random.randint(250, 569) / 1000)
                print(windows_obj.region_tool)
                bot_stage = 4

            # Loof for weapon pixel to know that you are done gathering
            elif bot_stage == 4:
                # print(windows_obj.region_tool)
                if pyautogui.locateOnScreen("imgs/weapon-1.png", grayscale=True, confidence=.75,
                                            region=windows_obj.region_weapon_1) is not None:
                    gathering_message = "Chopping with a wood axe"
                    print("4 - Gathering Message - ", gathering_message)
                    bot_stage = 5

            # Are we actually gathering some shit and if yes, what
            elif bot_stage == 5:
                if pyautogui.locateOnScreen("imgs/gather-lumbering-1.png", grayscale=True, confidence=.75,
                                            region=windows_obj.region_tool) is not None:
                    gathering_message = "Chopping with a wood axe"
                    print("4 - Gathering Message - ", gathering_message)
                    bot_stage = 6
                elif pyautogui.locateOnScreen("imgs/gather-mining-1.png", grayscale=True, confidence=.75,
                                              region=windows_obj.region_tool) is not None:
                    gathering_message = "Mining with an pick axe"
                    print("4 - Gathering Message - ", gathering_message)
                    bot_stage = 6
                elif pyautogui.locateOnScreen("imgs/gather-harvesting-1.png", grayscale=True, confidence=.75,
                                              region=windows_obj.region_tool) is not None:
                    gathering_message = "Harvesting with a sickle"
                    print("4 - Gathering Message - ", gathering_message)
                    bot_stage = 6
                else:
                    # Didn't actually start gathering anything so start over
                    print("4 - Gathering Message - Dosen't look like I am gathering anything so goto 0")
                    random_casting_delay = random.randint(150, 350) / 1000  # shorty distance
                    time.sleep(random_casting_delay)
                    bot_stage = 8

            # are we done gathering
            elif bot_stage == 6:
                #random_casting_delay = random.randint(10, 69) / 1000  # shorty distance
                #time.sleep(random_casting_delay)
                bot_stage = 7
            # are we done gathering
            elif bot_stage == 7:
                if pyautogui.locateOnScreen("imgs/gather-completed-1.png", grayscale=False, confidence=.95, region=windows_obj.region_tool) is not None:
                    print("7 - Gathering Completed")
                    duration_time = time.time() - start_time
                    print("(", gather_obj.getGatherCounter(), ") cycle gathering -", gathering_message , "in", round(duration_time,1), "seconds")
                    bot_stage = 8

            # Run to next spot
            elif bot_stage == 8:
                print("8 - Gathering Completed")
                key = '='
                #print("pressing =")
                time.sleep(0.3)
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
