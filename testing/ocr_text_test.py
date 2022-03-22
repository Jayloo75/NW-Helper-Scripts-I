import cv2
import pytesseract

# Path for Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read in image as grayscale
full_filename = "imgs/ocr_test_imageqty5.png"
image = cv2.imread(full_filename,0)
# Threshold to obtain binary image
thresh = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)[1]

# Create custom kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# Perform closing (dilation followed by erosion)
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Invert image to use for Tesseract
result = 255 - close
cv2.imshow('thresh', thresh)
cv2.imshow('close', close)
cv2.imshow('result', result)

# Throw image into tesseract
print(pytesseract.image_to_string(result))
cv2.waitKey()