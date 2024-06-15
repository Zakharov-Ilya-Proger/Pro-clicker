import pyautogui as pya
from random import randint
from time import sleep

w, h = pya.size()


def click_to_banana():
    sleep(10)
    pya.moveTo(w/2, h/2 + 50)
    for i in range(150):
        sleep(randint(1, 5) / 100)
        pya.click()
