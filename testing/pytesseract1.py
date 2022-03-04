import cv2
import pytesseract as tess
from pytesseract import Output
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image


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


# img = cv2.imread('imgs/text-test.png')
# img = cv2.imread('imgs/e0.png')
# img = cv2.imread('imgs/e-young-tree.png')
# img = cv2.imread('imgs/coords.png')

img = cv2.imread('imgs/pytesseract-test.png')

# img = get_grayscale(img)
# img = thresholding(img)
# img = remove_noise(img)


d = tess.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    print(d['text'][i])
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(d)
# print(d["text"])


# text_ocr = ocr_core(img)
# print(text_ocr[2])
# print(text_ocr[3])

while True:
    cv2.imshow("frame", img)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break

cv2.destroyAllWindows()