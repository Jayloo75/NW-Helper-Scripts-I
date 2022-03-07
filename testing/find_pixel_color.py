import numpy as np

import cv2 as cv
from numpy import array
from PIL import ImageGrab


img = ImageGrab.grab(bbox=(2327, 1126, 2328, 1127))
img_np = np.array(img)
print(img_np)
da_pixel = img.getpixel((1, 1))
print(da_pixel)



    # mask = cv.inRange(img, color_lower, color_upper)
