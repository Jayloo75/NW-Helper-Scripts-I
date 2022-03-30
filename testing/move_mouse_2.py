import ctypes
import time
import pydirectinput
from classes.windows_class import Windows

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions
def MouseMoveTo(x, y):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))

    command = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

def pyMove(x, y, duration, rate):
    steps = int(duration / rate)
    dx = (x) / steps
    dy = (y) / steps
    startTime = time.time()
    lagCount = 0
    for i in range(steps):
        # pydirectinput.move(int(x + i * dx), int(y + i * dy))
        MouseMoveTo(int(dx), int(dy))

        print(int(dx))
        try:
            time.sleep(rate * (i + 1) + startTime - time.time())
        except ValueError:
            lagCount += 1
    print(steps, lagCount)



windows_obj = Windows()
# windows_obj = Windows()

time.sleep(1.5)

pydirectinput.click()

time.sleep(1.5)

pyMove(7200, 0, 4, .5)  #  1800 moves from north to ease

# MouseMoveTo(100, 0)
# time.sleep(.25)
# MouseMoveTo(100, 100)
# time.sleep(.25)
# MouseMoveTo(-100, 0)
# time.sleep(.25)
# MouseMoveTo(-100, -100)

