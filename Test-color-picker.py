# Python program to identify
# color in images

# Importing the libraries OpenCV and numpy
import cv2
import numpy as np

import matplotlib.pyplot as plt
import PIL
#%matplotlib inline

# Read the images
#img = cv2.imread("imgs/shapes.jpg")
image = cv2.imread("imgs/success font.png")

# Convert Image to Image HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Defining lower and upper bound HSV values
lower = np.array([90, 50, 50])
upper = np.array([110, 255, 255])

# Defining mask for detecting color
mask = cv2.inRange(hsv, lower, upper)
#mask = cv2.inRange(hsv, (0, 50, 50), (20, 255, 255))

result = cv2.bitwise_and(image, image, mask= mask)

cv2.imwrite("imgs/shapes_orig.png", image)
cv2.imwrite("imgs/shapes_hsv.png", hsv)
cv2.imwrite("imgs/shapes_mask.png", mask)
cv2.imwrite("imgs/shapes_result.png", result)

#print(result)

img_temp = result
unique, counts = np.unique(img_temp.reshape(-1, 3), axis=0, return_counts=True)
#img_temp[:,:,0], img_temp[:,:,1], img_temp[:,:,2] = unique[np.argmax(counts)]

print(unique[0])
print(unique[1])
print(unique[2])
print(counts[0])
print(len(unique))
print(len(counts))


x = np.where(unique == [50, 46, 35])
#x = np.where(unique == [0, 0, 0])

print(x)

#for k in unique:
#    print(k)



#show_img_compar(img, img_temp)
