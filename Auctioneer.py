import pyautogui
import pydirectinput
import time
import random
import keyboard
import numpy as np
from PIL import ImageGrab, Image
from classes.windows_class import Windows
from tkinter import *
import cv2
import pytesseract as tess
from classes.NWDB import NWDB
import win32gui
from pytesseract import Output
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

nwdb_obj = NWDB()
# for row in nwdb_obj.get_auctioneer_resources():
#     print(row)
tp_items = nwdb_obj.get_auctioneer_resources()
# (16, 'Platinum Ingot', 'platinum-ingot.png', 'platinum Ing')
nwdb_obj.close()



def ocr_core(img):
    text = tess.image_to_string(img, config='--psm 6 -c tessedit_char_whitelist=0123456789.')
    return text


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 1)


def thresholding(image):
    return cv2.threshold(image, 245, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


def clicked(windows_obj, search_term_id):
    windows_obj.activate_new_world_window()
    pyautogui.write('/rec ', interval=0.05)
    print("debug---", search_term_id)
    print("debug---", tp_items[search_term_id])
    # pyautogui.write("testing 1=", tp_items[search_term_id])
    pyautogui.write("testing 1=" + str(tp_items[search_term_id][1]))


def get_price_and_qty(windows_obj):
    win = windows_obj.newWorldWindow
    vert_spacing = 77
    for row in range(0, 9):
        price_x1 = round(win.left + 969)
        price_x2 = round(price_x1 + 113)

        qty_x1 = round(win.left + 969 + 540)
        qty_x2 = round(qty_x1 + 64)

        # y1 = round(win.top + 433 + row * vert_spacing)
        # y2 = round(y1 + 31 + row * vert_spacing)
        y1 = round(win.top + 433 + row * vert_spacing)
        y2 = round(y1 + 31)

        # Get price for this row
        filename = "price_" + str(row) + ".png"
        price = get_ocr_result(windows_obj, price_x1, y1, price_x2, y2, filename)

        # Get qTY for this row
        filename = "qty" + str(row) + ".png"
        qty = get_ocr_result(windows_obj, qty_x1, y1, qty_x2, y2, filename)

        now = int(time.time())

        print(row, "--", price, "--", qty, "--", now)

    # move page down

    # pyautogui.keyDown(key)
    # auctioneer_scrollbar_1_x = round(win.left + 1848)
    # auctioneer_scrollbar_1_y = round(price_x1 + 453)
    # pydirectinput.click(auctioneer_scrollbar_1_x, auctioneer_scrollbar_1_y)


def are_you_still_playing(newWorldWindow):
    RegionX = round(newWorldWindow.left + 1381)
    RegionY = round(newWorldWindow.top + 75)
    RegionWidth = round(421)
    RegionHeight = round(62)
    region_still_playing = (RegionX, RegionY, RegionWidth, RegionHeight)
    print("region_still_playing", region_still_playing)

    print("Checking region_still_playing region")
    # Are you still Playing - how to deal with this - set a trigger then at most convienient time move character
    if pyautogui.locateOnScreen("imgs/still_playing_TP.png", grayscale=False, confidence=.65,
                                region=region_still_playing) is not None:
        print("Yes, I am still playing!")
        return True
    else:
        return False


# Function to move character as to get rid of "Are you still playing?" Message
def move_player_char():
    move_direction = ["a", "d"]
    # Move forward then back for a sec
    key = move_direction[random.randint(0, 1)]
    pyautogui.keyDown(key)
    time.sleep(random.randint(70, 170) / 1000)
    pyautogui.keyUp(key)


def get_ocr_result(windows_obj, x1, y1, x2, y2, filename):
        bbox_price_and_qty_ocr = (x1, y1, x2, y2)
        # print("bbox_price_and_qty_ocr", bbox_price_and_qty_ocr)

        img = ImageGrab.grab(bbox=bbox_price_and_qty_ocr)  # x1,y1,x2,y2

        width, height = img.size
        # ratio = floor(height / width)
        # newheight = ratio * 500
        ratio_multiplier = 3
        img = img.resize((width*ratio_multiplier, height*ratio_multiplier))

        full_filename1 = "testing/imgs/ocr_test_image1_" + filename
        full_filename2 = "testing/imgs/ocr_test_image2_" + filename
        # print(full_filename)
        img.save(full_filename1)
        img_np = np.array(img)
        img_frame = img_np

        # hsv = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
        # lower = np.array([333, 70, 65])
        # upper = np.array([313, 44, 42])
        # mask = cv2.inRange(hsv, lower, upper)


        img_frame = get_grayscale(img_np)
        img_frame = thresholding(img_frame)

        # inverted = np.invert(img_frame)
        cv2.imwrite(full_filename2, img_frame);




        coords_string = ocr_core(img_frame)
        newstr = coords_string.strip()
        # print(coords_string)
        return(newstr)


def open_trading_post():
    pydirectinput.press('e')

def exit_trading_post():
    pydirectinput.press('esc')

# delay for pausing code execution in milliseconds
def delay_random(min_sec=350, max_sec=970):
    time.sleep(random.randint(min_sec, max_sec) / 1000)


def search_items(windows_obj, search_term_id):
    newWorldWindow = windows_obj.newWorldWindow

    if are_you_still_playing(newWorldWindow) == True:
        delay_random(170,250)
        exit_trading_post()
        delay_random(589,1200)
        move_player_char()
        delay_random(589,1200)
        open_trading_post()
        delay_random(589,1200)

    print("debug---", search_term_id)
    print("debug---", tp_items[search_term_id][1])


    RegionX = round(newWorldWindow.left + 627)
    RegionY = round(newWorldWindow.top + 296)
    RegionWidth = round(RegionX + 49)
    RegionHeight = round(RegionY + 51)
    windows_obj.region_auctioneer_refresh = (RegionX, RegionY, RegionWidth, RegionHeight)
    print("windows_obj.region_auctioneer_refresh", windows_obj.region_auctioneer_refresh)

    RegionX = round(newWorldWindow.left + 86)
    RegionY = round(newWorldWindow.top + 284)
    RegionWidth = round(230)
    RegionHeight = round(57)
    region_auctioneer_search_items_box = (RegionX, RegionY, RegionWidth, RegionHeight)
    print("region_auctioneer_search_items_box", region_auctioneer_search_items_box)

    # Searchable region for search dropdown
    RegionX = round(newWorldWindow.left + 106)
    RegionY = round(newWorldWindow.top + 358)
    RegionWidth = round(RegionX + 467)
    RegionHeight = round(RegionY + 495)
    region_auctioneer_search_dropdown = (RegionX, RegionY, RegionWidth, RegionHeight)
    bot_stage = 0

    cycler = True
    bot_stage = 0

    # while 1:
    while cycler:

        auctioneer_refresh_clickable_x = newWorldWindow.left + 635 + random.randint(0, 32)
        auctioneer_refresh_clickable_y = newWorldWindow.top + 310 + random.randint(0, 26)

        # auctioneer_search_clickable_x = newWorldWindow.left + 150 + random.randint(0, 300)
        # auctioneer_search_clickable_y = newWorldWindow.top + 321 + random.randint(0, 18)

        auctioneer_search_clickable_x = newWorldWindow.left + 100 + random.randint(0, 489)
        auctioneer_search_clickable_y = newWorldWindow.top + 296 + random.randint(0, 41)


        # Initial default state - reset any variables here
        if bot_stage == 0:
            print(bot_stage, " -------------- Starting -----------------")
            bot_stage = 50

        # make sure that the box is available to write in
        elif bot_stage == 50:
            print(bot_stage, " Start looking for SEARCH ITEMS box")
            print(bot_stage, "region_auctioneer_search_items_box", region_auctioneer_search_items_box)
            search_image_name = "imgs/auctioneer-search-items-box.png"
            search_items_box = pyautogui.locateOnScreen(search_image_name, grayscale=True, confidence=.75,
                                        region=region_auctioneer_search_items_box)

            if search_items_box is not None:
                # print(search_dropdown_coords)
                # print(bot_stage, " search_items_box", search_items_box)
                bot_stage = 100
            else:
                time.sleep(random.randint(250, 780) / 1000)  # shorty distance




        # Click into the search box at a random location
        elif bot_stage == 100:
            print(bot_stage, " Click the search box")
            pydirectinput.click(auctioneer_search_clickable_x, auctioneer_search_clickable_y)
            time.sleep(random.randint(150, 340) / 1000)  # shorty distance
            pydirectinput.click(auctioneer_search_clickable_x, auctioneer_search_clickable_y)
            bot_stage = 101

        #pause for a quick second
        elif bot_stage == 101:
            print(bot_stage, " A quick random wait timer")
            time.sleep(random.randint(450, 800) / 1000)  # shorty distance
            # cycler = False
            bot_stage = 102

        # type "oil"
        elif bot_stage == 102:
            print(bot_stage, " Type ", tp_items[search_term_id][1])
            pyautogui.write(tp_items[search_term_id][3], interval=0.09)
            bot_stage = 103

        # Locate "oil in drop down and click it
        elif bot_stage == 103:
            search_image_name = "imgs/search/" + tp_items[search_term_id][2]
            search_dropdown_coords = pyautogui.locateOnScreen(search_image_name, grayscale=True, confidence=.75,
                                        region=region_auctioneer_search_dropdown)
            if search_dropdown_coords is not None:
                # print(search_dropdown_coords)
                print(bot_stage, " search_dropdown_coords", search_dropdown_coords)
                # time.sleep(random.randint(250, 780) / 1000)  # shorty distance
                bot_stage = 104

            # click the search result
        elif bot_stage == 104:
            # time.sleep(random.randint(450, 880) / 1000)  # shorty distance
            search_dropdown_coords_clickable_x = search_dropdown_coords[0] + random.randint(0, search_dropdown_coords[2])
            search_dropdown_coords_clickable_y = search_dropdown_coords[1] + random.randint(0, search_dropdown_coords[3])

            print(bot_stage, " Debug", search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)
            pydirectinput.click(search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)

            print(bot_stage, " Debug", search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)
            #print(bot_stage, " Debug", search_dropdown_coords_clickable_x, search_dropdown_coords_clickable_y)

            bot_stage = 105

        elif bot_stage == 105:
            # now read some shit
            print(bot_stage, " Let's read some numbers ")
            time.sleep(random.randint(750, 1280) / 1000)  # shorty distance
            get_price_and_qty(windows_obj)

            print(bot_stage, " done: Next! ")
            bot_stage = 106

            #
        elif bot_stage == 106:


            print(bot_stage, " Dead end!`")
            cycler = False
            # bot_stage = 69



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
        # if keyboard.is_pressed('f1'):
        #     print("\nyou pressed F1, so resuming...")
        #     cycler = True

def main():
    """
    Main function for the program
    """
    print("main function Initiated")


    # Initiate windows class
    windows_obj = Windows()

    window = Tk()
    window_title = "Auctioneer"
    window.title(window_title)
    window.geometry('800x600')

    row_counter = 0
    for item in tp_items:
        # print(item)
        the_text = item[1]
        # the_text = item[1], "#", row_counter
        # btn = tk.Button(my_w, text=language, command=lambda lan=language:show_lan(lan))
        # Button(window, text=the_text, command=lambda: clicked(windows_obj, row_counter)).grid(column=0, row=row_counter)
        # Button(window, text=the_text, command=partial(clicked, windows_obj, row_counter)).grid(column=0, row=row_counter)
        Button(window, width=20, text=str(the_text), command=lambda win=windows_obj, rc=row_counter: search_items(win, rc)).grid(column=0, row=row_counter)

        # tk.Button(self.board, command=lambda i=i, j=j: self.on_click(i, j))

        row_counter = row_counter + 1

    # btn1 = Button(window, text="Oil", command=lambda: clicked(windows_obj, "Oil"))
    # btn1.grid(column=0, row=0)
    #
    # btn2 = Button(window, text="Iron Ore", command=lambda: clicked(windows_obj, "Iron Ore"))
    # btn2.grid(column=0, row=1)

    window.mainloop()

    # time.sleep(random.randint(250, 251) / 1000)  # shorty distance
    # hwnd = win32gui.FindWindow(None, window_title)
    # win32gui.MoveWindow(hwnd, 100, 275, 250, 500, True)


# Runs the main function
if __name__ == '__main__':
    main()
