import win32api
from easing_functions import *
import time

# pos = (200, 200)
# win32api.SetCursorPos(pos)


def move_smooth(xm, ym, t):
    for i in range(t):
        if i < t/2:
            h = i
        else:
            h = t - i
        #mouse.move(h*xm, h*ym)
        pos = (h*xm, h*ym)
        win32api.SetCursorPos(pos)
        time.sleep(1/60)


#move_smooth(222, 222, 40)



# For a duration 10 you will get the relevant output from start to end
a = QuadEaseInOut(start=0, end = 3, duration = 10)
k = a.ease(4) # 4 is a number between 0 and the duration you specified
#k is the returned value from start to end (0 to 3)
k2 = a(4) # the ease object can also be called directly, like a function

# example plots:
import numpy as np
import matplotlib.pyplot as plt

a = BounceEaseInOut(start=3, end=1, duration=1)
b = BounceEaseIn(start=0, end=1)
c = BounceEaseOut(start=0, end=1)

x = np.arange(0, 1, 0.001)
y0 = list(map(a, x))
y1 = list(map(b, x))
y2 = list(map(c, x))

plt.plot(x,y0)
plt.plot(x,y1)
plt.plot(x,y2)

