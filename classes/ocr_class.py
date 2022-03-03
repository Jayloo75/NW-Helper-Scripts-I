import cv2
import pytesseract as tess

class Ocr:
    # tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def ocr_core(self, img):
        # text = tess.image_to_string(img, config='-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        # text = tess.image_to_string(img, config='-h 8')
        # text = tess.image_to_string(img, config='-h 8')
        text = tess.image_to_string(img)
        return text

    def get_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def remove_noise(self, image):
        return cv2.medianBlur(image, 1)

    def thresholding(self, image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # imagergb = ImageGrab.grab(bbox=(1148, 1059, 1398, 1118))  # x1,x2,y1,y2
    # img_np = np.array(imagergb)
    # print(img_np)

    ###print("Keep Reeling em in - step:" + str(bot_stage))
    # time_now = time.time()
    ###print("Image Grab - " + str(     round(time_now-last_time, 2) )        )
    # last_time = time_now
    # img = ImageGrab.grab(bbox=(1148, 1059, 1398, 1118))  # x1,x2,y1,y2
    # img_np = np.array(img)
    # print(img_np)
    # img_frame = get_grayscale(img_np)
    # img_frame = thresholding(img_frame)
    # coords_string = ocr_core(img_frame)
    # newstr = coords_string.strip()
    # array_length = len(newstr.split())
    # if array_length > 0 and newstr == 'SUCCESS!':
    #    print("[Fish Caught]" + newstr + "[Fish Caught]")
    #    if mouse_click_down == 1:
    #        print("Found that mouse_click_down == 1 so sending mouseuo command.")
    #        pyautogui.mouseUp()
    # casting_switch = 0
    #    bot_stage = 0