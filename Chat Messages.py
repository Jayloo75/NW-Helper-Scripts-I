import pyautogui
import pydirectinput
import time
import random
import keyboard
import sys
import array
from classes.windows_class import Windows
from classes.gather import Gather

from tkinter import *
from tkinter import scrolledtext

messages1 = "Phoenix Rizing (formally Bound on Pickup) is recruiting active Syndicate players of all levels for pvp/pve.  DM me for an invite."
messages2 = "Phoenix Rizing (formally Bound on Pickup) (syn) is recruiting all levels!  We are laid back, friendly group who hang out and have fun in vc.  We do PvP and PvE content.  We also host the nightly Harry Zerg.  DM if interrested."
messages3 = "Phoenix Rizing (formally Bound on Pickup) (syn) is recruiting all levels!  We are laid back, friendly group who hang out and have fun in vc.  We do PvP and PvE content.  DM if interrested."
messages4 = "Phoenix Rizing (formally Bound on Pickup) (syn) is recruiting all levels!  We are 86 members strong and 65 have been online in the last 24 hours. We do PvP and PvE content.  DM if interrested."

print(len(messages2))
windows_obj = Windows()

window = Tk()
window.title("New World Messages App")
window.geometry('580x500')

# lbl = Label(window, text="Hello")
# lbl.grid(column=1, row=0)


def clicked1():
    windows_obj.activate_new_world_window()
    pyautogui.write('/rec ', interval=0.05)
    pyautogui.write(messages1)


def clicked2():
    windows_obj.activate_new_world_window()
    pyautogui.write('/rec ', interval=0.05)
    pyautogui.write(messages2)


def clicked3():
    windows_obj.activate_new_world_window()
    pyautogui.write('/rec ', interval=0.05)
    pyautogui.write(messages3)


def clicked4():
    windows_obj.activate_new_world_window()
    pyautogui.write('/rec ', interval=0.05)
    pyautogui.write(messages4)


btn1 = Button(window, text="Paste", command=clicked1)
btn1.grid(column=0, row=0)
txt1 = scrolledtext.ScrolledText(window,width=60,height=5)
txt1.insert(INSERT,messages1)
txt1.grid(column=1,row=0)

btn2 = Button(window, text="Paste", command=clicked2)
btn2.grid(column=0, row=1)
txt2 = scrolledtext.ScrolledText(window,width=60,height=5)
txt2.insert(INSERT,messages2)
txt2.grid(column=1,row=1)

btn3 = Button(window, text="Paste", command=clicked3)
btn3.grid(column=0, row=2)
txt3 = scrolledtext.ScrolledText(window,width=60,height=5)
txt3.insert(INSERT,messages3)
txt3.grid(column=1,row=2)

btn4 = Button(window, text="Paste", command=clicked4)
btn4.grid(column=0, row=3)
txt4 = scrolledtext.ScrolledText(window,width=60,height=5)
txt4.insert(INSERT,messages4)
txt4.grid(column=1,row=3)

window.mainloop()