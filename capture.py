import numpy as np
import cv2
from PIL import ImageGrab
import pytesseract as tess
import re
import time
import pyautogui
import random
import pydirectinput
import keyboard
import sys


tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def ocr_core(img):
    #custom_config = r'--oem 3 --psm 6 outputbase digits'
    custom_config = r' --psm 8 -c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,!?*@[]{}();:%-_~‘¢`“/'
    text = tess.image_to_string(img, config=custom_config)
    #print(text)

    ####text = tess.image_to_string(img, config='-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,!?*@[]{}();:%-_`')

    #tess.image_to_string(question_img, config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6")
    #text = tess.image_to_string(img, config='-c preserve_interword_spaces=1 tessedit_char_whitelist=0123456789. tessedit_char_blacklist={}[](),}')
    #text = tess.image_to_string(img, config='-c preserve_interword_spaces=1 -c tessedit_char_whitelist=0123456789. ')
    #text = tess.image_to_string(img, config='-c preserve_interword_spaces=1')
    #text = tess.image_to_string(img)
    return text

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 1)

def thresholding(image):
    return cv2.threshold(image, 235, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]



def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def iscoord(float):
    string = str(float)
    parts = string.split(".")
    #print(parts)

    if 3 <= len(parts[0]) <= 5 and len(parts[1]) ==3 and round(float, 3) == float:
        return True
    else:
        #print('false')
        return False



    # parts = string.split(".")
    # string = str(string)
    # #result = re.match('^[0-9]{4}\.[0-9]{3}$', string)
    # #result = re.match('\d{4}\.\d{3}', string)
    # result = re.search('^([0-9]{4})(\.)([0-9]{3})$', string)
    # if result:
    #     #print('true')
    #     return True
    # else:
    #     #print('false')
    #     return False

    # Finds all Windowss with the title "New World"
newWorldWindows = pyautogui.getWindowsWithTitle("New World")

# Find the Window titled exactly "New World" (typically the actual game)
for window in newWorldWindows:
    if window.title == "New World":
        newWorldWindow = window
        break

# Randomly will move right or left to keep from AFKing
moveDirection = ["a", "d"]

# Select that Window
newWorldWindow.activate()
print("NW Window Location x=", newWorldWindow.left, " z=", newWorldWindow.top,
      " width=", newWorldWindow.width, " height", newWorldWindow.height, )
# Move your mouse to the center of the game window
centerW = newWorldWindow.left + (newWorldWindow.width / 2)
centerH = newWorldWindow.top + (newWorldWindow.height / 2)
pyautogui.moveTo(centerW, centerH)

time.sleep(random.randint(254, 652) / 1000)
pyautogui.click()


x1_coord = int(newWorldWindow.width + newWorldWindow.left - 290)
x2_coord = int(newWorldWindow.left + newWorldWindow.width - 10)
y1_coord = int(newWorldWindow.top + 50)
y2_coord = int(newWorldWindow.top + 67)
bbox_coord = (x1_coord, y1_coord, x2_coord, y2_coord)
#print (x1_coord, y1_coord, x2_coord, y2_coord)

x1_coord = int(newWorldWindow.width + newWorldWindow.left - 1100)
x2_coord = int(newWorldWindow.left + newWorldWindow.width - 800)
y1_coord = int(newWorldWindow.top + 30)
y2_coord = int(newWorldWindow.top + 90)
bbox_compas = (x1_coord, y1_coord, x2_coord, y2_coord)
#print (x1_coord, y1_coord, x2_coord, y2_coord)


#pyautogui.press('w')

start_time = time.time()
last_time = time.time()


#filename = 'imgs/coords.png'
def capture_start_direction():
    global start_direction
    img1 = np.array(ImageGrab.grab(bbox=(bbox_compas)))
    img2 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    start_direction = img2
    cv2.imshow('window start', img2)
    return

def SeekRightDirection():
    pydirectinput.move(5, 100)

def capture_compas():
    img1 = np.array(ImageGrab.grab(bbox=(bbox_compas)))
    img2 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    cv2.imshow('window capturel', img2)
    return img2

def is_template_present(image, template, threshold=0.9):
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = .9
    loc = np.where(res >= threshold)
    return len(loc[0]) > 0

def Is_Facing_Saved_Direction():
    print("Seeking right direction")
    global start_direction
    img = capture_compas()
    return is_template_present(img, start_direction, .6)


time.sleep(1)
capture_start_direction()
print("ok to move - 5 secs")

time.sleep(5)

# while (Is_Facing_Saved_Direction() == False):
#     print("Seeking right direction")
#     SeekRightDirection()
#     if keyboard.is_pressed('Esc'):
#         print("\nyou pressed Esc, so exiting...")
#         sys.exit(0)


while True:



    # def Is_Facing_Saved_Direction(self):
    #     img = self.capture_compas()
    #     return self.is_template_present(img, self.start_direction, .6)








    #img = ImageGrab.grab(bbox=(2290, 18, 2560, 35))  # x1,x2,y1,y2
    # img = ImageGrab.grab(bbox=(2300, 18, 2560, 35))  # x1,y1,X2,y2
    # img = ImageGrab.grab(bbox=(bbox_coord))  # x1,y1,X2,y2
    img = ImageGrab.grab(bbox=(bbox_coord))  # x1,y1,X2,y2
    img_np = np.array(img)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    #cv2.imwrite(filename, frame)

    img_frame = get_grayscale(img_np)
    img_frame = thresholding(img_frame)
    #img_frame = remove_noise(img_frame)
    coords_string = ocr_core(img_frame)
    newstr = coords_string.strip()
    array_length = len(newstr.split())
    # print("[startraw]]" + str(newstr.split()) + "[endraw]")
    #cv2.imshow("frame", img_frame)

    split_coords = newstr.split()
    # print("[split_coords]]" + str(split_coords) + "[split_coords]")
    # print("[array_length]]" + str(array_length) + "[array_length]")

    if array_length >= 2:
        float_x = split_coords[0].strip(".")
        float_y = split_coords[1].strip(".")
        # print("[float_x]]", float_x, float_y,  "[float_x]")

        if isfloat(float_x) and isfloat(float_y):
            float_x = float(float_x)
            float_y = float(float_y)
            #print("[X]" + str(float_x) + "[Y]" + str(float_y))

        #if array_length == 3:
            #print("[start]]" + newstr + "[end]")
            #print(len(newstr.split()))

            #print("-----------------------------------------------")
            #print("newstr = ",newstr)
            #split_coords = newstr.split()
            #print(split_coords)

            #check_float_x = isinstance(split_coords[0], float)
            #check_float_y = isinstance(split_coords[1], float)

            #if isfloat(split_coords[0]) and isfloat(split_coords[1]):
            #    float_x = float(split_coords[0])
            #    float_y = float(split_coords[1])

            if iscoord(float_x) and iscoord(float_y):
                #if check_float_x and check_float_y:
                coord_timer = round(time.time()-last_time, 1)
                print("x=",float_x ,"      y=" , float_y, "t=", coord_timer)
                last_time = time.time()
                #print("x=",round(float_x, 4) ,"      y=" , round(float_y, 3))
                #print(check_float_x)




    cv2.imshow("frame", img_frame)

    if cv2.waitKey(1) & 0Xff == ord('q'):
        break

    if keyboard.is_pressed('Esc'):
        print("\nyou pressed Esc, so exiting...")
        sys.exit(0)

cv2.destroyAllWindows()
