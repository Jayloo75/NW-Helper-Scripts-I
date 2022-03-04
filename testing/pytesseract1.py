import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract as tess
from pytesseract import Output
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def ocr_core(img):
    # tess.image_to_string(question_img, config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6")
    # text = tess.image_to_string(img, config='-c tessedit_char_whitelist=0123456789.[]    ')
    text = tess.image_to_string(img)
    return text


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 10)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]



# img = ImageGrab.grab(bbox=(1300, 525, 1416, 562))  # x1,y1,x2,y2
# img = ImageGrab.grab(bbox=(1300, 1141, 1416, 1178))  # x1,y1,x2,y2
img = ImageGrab.grab(bbox=(1829, 1141, 1891, 1178))  # x1,y1,x2,y2
img_np = np.array(img)
# print(img_np)
img_frame = get_grayscale(img_np)
img_frame = thresholding(img_frame)
coords_string = ocr_core(img_frame)
newstr = coords_string.strip()
print(newstr)







# d = tess.image_to_data(img, output_type=Output.DICT)
# n_boxes = len(d['level'])
# for i in range(n_boxes):
#     print(d['text'][i])
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# print("Asdf")
# # print(d["text"])
#
#
# text_ocr = ocr_core(img)
# print(text_ocr)

# while True:
#     cv2.imshow("frame", img)
#     if cv2.waitKey(1) & 0Xff == ord('q'):
#         break
#
# cv2.destroyAllWindows()