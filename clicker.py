from time import sleep
import keyboard

from click.click_to_banana import click_to_banana
from click.find_icon import find_and_open, find_close


is_clicking = False
hours = 0


def clicking():
    global is_clicking
    is_clicking = not is_clicking
    if is_clicking:
        print("Now we are clicking")
    else:
        print("Stop clicking")


keyboard.add_hotkey("ctrl+alt+b", lambda: clicking())
while True:
    if hours % 3 == 0 or hours % 17 == 0:
        if is_clicking:
            print("We are in work")
            find_and_open()
            click_to_banana()
            find_close()
        else:
            continue
    else:
        sleep(3600)
        hours += 1
