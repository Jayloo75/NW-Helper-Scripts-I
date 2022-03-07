import pyautogui
import pydirectinput
import time
import random
import keyboard
import sys

class Windows:
    # Attributes
    newWorldWindows = False
    newWorldWindow = False
    left             = False
    width            = False
    top              = False
    height           = False
    region_full_window = False
    debug = True

    #Methods
    def __init__(self):
        #Windows = Windows()
        self.getNewWorldWindow()
        self.activate_new_world_window()
        self.moveMouseToCenterOfWindow()
        self.getRegionFullWindow()
        self.region_gather()
        self.region_tool()
        self.region_weapon_1()
        #self.clickWindow()

    def getNewWorldWindow(self):
        # Finds all Windows with the title "New World"
        self.newWorldWindows = pyautogui.getWindowsWithTitle("New World")

        # Find the Window titled exactly "New World" (typically the actual game)
        for window in self.newWorldWindows:
            if window.title == "New World":
                self.newWorldWindow = window
                self.left = self.newWorldWindow.left
                self.width = self.newWorldWindow.width
                self.top = self.newWorldWindow.top
                self.height = self.newWorldWindow.height
                break
        if not self.newWorldWindow:
            sys.exit('New World Window Not Found')
        return self.newWorldWindow

    def activate_new_world_window(self):
        # Select that Window
        self.newWorldWindow.activate()
        return True

    # Move your mouse to the center of the game window
    def moveMouseToCenterOfWindow(self):

        print("hellerg")
        # newWorldWindow = self.newWorldWindow
        centerW = self.left + (self.width / 2)
        centerH = self.top + (self.height / 2)
        pyautogui.moveTo(centerW, centerH)

    # Get deets of full window position and size
    def getRegionFullWindow(self):
        # newWorldWindow = Windows.newWorldWindow
        self.region_full_window = (self.left,
                                    self.top,
                                    self.width,
                                    self.height)
        if self.debug:
            print("New World window location:", self.region_full_window)

    def region_gather(self):
        # Windows.region_gather
        # newWorldWindow = Windows.newWorldWindow
        region_x = round(self.left + self.width * 0.36)
        region_y = round(self.top + self.height * 0.36)

        region_width = round(self.left + self.width * 0.55)
        region_height = round(self.top + self.height * 0.70)
        Windows.region_gather = (region_x, region_y, region_width, region_height)

    def region_tool(self):
        # Windows.region_gather
        # newWorldWindow = Windows.newWorldWindow
        region_x = round(self.left + self.width - 300)
        region_y = round(self.top + self.height - 200)

        region_width = round(300)
        region_height = round(200)
        Windows.region_tool = (region_x, region_y, region_width, region_height)

    def region_weapon_1(self):
        # Windows.region_gather
        # newWorldWindow = Windows.newWorldWindow
        region_x = round(self.left + self.width - 58)
        region_y = round(self.top + self.height - 223)

        region_width = round(50)
        region_height = round(50)
        Windows.region_weapon_1 = (region_x, region_y, region_width, region_height)

    def clickWindow(self):
        time.sleep(.1)
        pyautogui.click()
        time.sleep(.1)