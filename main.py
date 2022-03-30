import pyautogui
import pydirectinput
import pygetwindow as gw
#import pyperclip as pc
import time

#Point(x=982, y=688)
#print (pyautogui.position())


pyautogui.moveTo(982, 688)

newWorldWindow = gw.getWindowsWithTitle('New World')[0]
newWorldWindow.activate()


time.sleep(1)
pydirectinput.click(982, 688)
time.sleep(1)
pydirectinput.keyDown('e')
time.sleep(1)
pydirectinput.keyUp('e')

print("That's all Folks!")
exit()

print("Tooooooooo Faaaaaaaarrrrrrrrr!")
pydirectinput.moveTo(100, 150)  # Move the mouse to the x, y coordinates 100, 150.
pydirectinput.click()  # Click the mouse at its current location.
pydirectinput.click(200, 220)  # Click the mouse at the x, y coordinates 200, 220.
pydirectinput.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
pydirectinput.doubleClick()  # Double click the mouse at the
pydirectinput.press('esc')  # Simulate pressing the Escape key.
pydirectinput.keyDown('shift')
pydirectinput.keyUp('shift')


exit()












#print (pyautogui.position())

exit()


#pyautogui.moveTo(391,342)
pyautogui.moveTo(850,731)
print("Move Mouse to 850,731")
print("Move Mouse to 850,731")

time.sleep(0.5)
pyautogui.click()


pyautogui.keyDown('w')
time.sleep(0.5)
pyautogui.keyUp('w')


#pyautogui.move(None, 10)

#pyautogui.typewrite("hello World")
#pyautogui.typewrite(["enter"])


#pyautogui.click(413,64)

#pyautogui.keyDown('ctrl')
#pyautogui.press('c')
#pyautogui.keyUp('ctrl')

#time.sleep(1)

#pyautogui.typewrite("hello World")
#pyautogui.typewrite(["enter"])

#Point(x=211, y=63)

#a = pc.paste()
#print(a)
#pyautogui.alert('This displays some text with an OK button.')