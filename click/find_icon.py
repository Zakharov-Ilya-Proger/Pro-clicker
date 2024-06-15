import pyautogui as pya

w, h = pya.size()
pya.FAILSAFE = False


def find_and_open():
    global w, h
    pya.moveTo(w / 2, h / 2)
    pya.doubleClick()
    print("Banana is open")


def find_close():
    global w, h
    pya.moveTo(w/2 + 500, h/2 - 400)
    pya.click()
    print("Banana is close")
