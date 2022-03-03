import pyautogui
import pydirectinput
import time
import random
import sys
import keyboard
import cv2
import time
import threading

import numpy as np
from PIL import ImageGrab
import pytesseract as tess
import win32api
from classes.windows_class import Windowss
from skimage.metrics import structural_similarity as compare_ssim
import argparse
import imutils

class Edge_Detection:
    original_image_check = False
    original_image = False
    windows_obj = False

    def showFishingDiff(self):
        RegionX = round(self.windows_obj.left + self.windows_obj.width * 0.05)
        RegionY = round(self.windows_obj.top + self.windows_obj.height * 0.1)
        RegionWidth = round(self.windows_obj.left + self.windows_obj.width * 0.70)
        RegionHeight = round(self.windows_obj.top + self.windows_obj.height * 0.28)
        region_Fishing_compare = (RegionX, RegionY, RegionWidth, RegionHeight)
        image = pyautogui.screenshot(region=region_Fishing_compare)

        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img_blur = image
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        # Display Canny Edge Detection Image
        scale_percent = 40  # percent of original size
        width = int(edges.shape[1] * scale_percent / 100)
        height = int(edges.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(edges, dim, interpolation=cv2.INTER_AREA)

        if self.original_image_check is False:
            self.original_image = edges
            original_image_resized = resized
            cv2.imshow('Original Image', original_image_resized)
            original_image_check = True

        # lets compare the 2 images
        (score, diff) = compare_ssim(original_image, edges, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))

        # cv2.imshow('DIFF', diff)
        cv2.imshow('Canny Edge Detection', resized)
        cv2.waitKey(10)
