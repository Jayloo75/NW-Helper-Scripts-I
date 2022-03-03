import pyautogui
import pydirectinput
import time
import random
import keyboard
import sys


class Gather:
    # Attributes
    gatherCounter = 0

    # Methods
    def getGatherCounter(self):
        return self.gatherCounter

    def incrementGatherCounter(self):
        self.gatherCounter = self.gatherCounter + 1