import pyautogui
import pydirectinput
import time
import random
import keyboard
import sys
from classes.windows_class import Windows
# from classes.gather import Gather
from classes.gather import Gather


def main():
    """
    Main function for the program
    """
    print("main function Initiated")# Initiate windows class
    windows_obj = Windows()

    newWorldWindow = windows_obj.newWorldWindow
    RegionX = round(newWorldWindow.left + 627)
    RegionY = round(newWorldWindow.top + 296)
    RegionWidth = round(RegionX + 49)
    RegionHeight = round(RegionY + 51)
    windows_obj.region_auctioneer_refresh = (RegionX, RegionY, RegionWidth, RegionHeight)
    print("windows_obj.region_auctioneer_refresh", windows_obj.region_auctioneer_refresh)


    # Searchable region for search dropdown
    RegionX = round(newWorldWindow.left + 106)
    RegionY = round(newWorldWindow.top + 358)
    RegionWidth = round(RegionX + 467)
    RegionHeight = round(RegionY + 495)
    region_auctioneer_search_dropdown = (RegionX, RegionY, RegionWidth, RegionHeight)




    cycler = True
    bot_stage = 0

    while 1:
        while cycler:

            auctioneer_refresh_clickable_x = newWorldWindow.left + 635 + random.randint(0, 32)
            auctioneer_refresh_clickable_y = newWorldWindow.top + 310 + random.randint(0, 26)

            auctioneer_search_clickable_x = newWorldWindow.left + 150 + random.randint(0, 300)
            auctioneer_search_clickable_y = newWorldWindow.top + 321 + random.randint(0, 18)


            # Initial default state - reset any variables here
            if bot_stage == 0:
                print(bot_stage, " -------------- Starting -----------------")
                bot_stage = 100

            # Click into the search box at a random location
            elif bot_stage == 100:
                print(bot_stage, " Click the search box")
                pydirectinput.click(auctioneer_search_clickable_x, auctioneer_search_clickable_y)
                bot_stage = 101

            #pause for a quick second
            elif bot_stage == 101:
                print(bot_stage, " A quick random wait timer")
                time.sleep(random.randint(450, 800) / 1000)  # shorty distance
                bot_stage = 102

            # type "oil"
            elif bot_stage == 102:
                print(bot_stage, " Type OIL")
                pyautogui.press('o')
                time.sleep(random.randint(110, 345) / 1000)  # shorty distance
                pyautogui.press('i')
                time.sleep(random.randint(110, 387) / 1000)  # shorty distance
                pyautogui.press('l')
                time.sleep(random.randint(201, 576) / 1000)  # shorty distance
                bot_stage = 103

            # Locate "oil in drop down and click it
            elif bot_stage == 103:
                search_dropdown_coords = pyautogui.locateOnScreen("imgs/auctioneer-search-dropdown-oil.png", grayscale=True, confidence=.75,
                                            region=region_auctioneer_search_dropdown)
                if search_dropdown_coords is not None:
                    # print(search_dropdown_coords)
                    print(bot_stage, " search_dropdown_coords", search_dropdown_coords)
                    time.sleep(random.randint(250, 780) / 1000)  # shorty distance
                    bot_stage = 104

                # click the search result
            elif bot_stage == 104:
                print(bot_stage, "Click eeeet!")
                print(search_dropdown_coords[0])
                print(search_dropdown_coords[1])
                print(search_dropdown_coords[2])
                print(search_dropdown_coords[3])

                search_dropdown_coords_clickable_x = newWorldWindow.left + 116 + random.randint(0, search_dropdown_coords[2])
                search_dropdown_coords_clickable_y = newWorldWindow.top + 695 + random.randint(0, search_dropdown_coords[3])

                print(bot_stage, " Debug", search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)
                pydirectinput.click(search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)

                print(bot_stage, " Debug", search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)
                #print(bot_stage, " Debug", search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)

                bot_stage = 105

            elif bot_stage == 105:
                bot_stage = 106

                #
            elif bot_stage == 106:


                print(bot_stage, " Dead end!`")
                bot_stage = 69






















            # Find the Interactable "E"
            elif bot_stage == 1:
                # Find that image on screen, in that region, with a confidence of 65%
                #if pyautogui.locateOnScreen("imgs/e0.png", grayscale=True, confidence=.65, region=region) is not None:
                if pyautogui.locateOnScreen("imgs/auctioneer-refresh.png", grayscale=True, confidence=.85, region=windows_obj.region_auctioneer_refresh) is not None:
                    print("1 - I found an interactable Object")
                    start_time = time.time()
                    bot_stage = 2

            # let's check some shit
            elif bot_stage == 2:
                print("2 - Lets click it")
                # let's wait a few then click on the refresh button
                pydirectinput.click(auctioneer_refresh_clickable_x, auctioneer_refresh_clickable_y)

                random_casting_delay = random.randint(9150, 25350) / 1000  # shorty distance
                time.sleep(random_casting_delay)

                bot_stage = 0






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
