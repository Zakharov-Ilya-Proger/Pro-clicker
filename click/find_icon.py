import pyautogui as pya
from time import sleep

w, h = pya.size()
pya.FAILSAFE = False

width = 250
height = 300


def find_and_open():
    global w, h
    pya.moveTo(w / 2, h / 2 + 50)
    pya.click()
    pya.sleep(1)
    pya.doubleClick()
    print("Banana is open")


def find_close():
    global w, h
    pya.moveTo(w/2 + width, h/2 - height)
    pya.click()
    print("Banana is close")
