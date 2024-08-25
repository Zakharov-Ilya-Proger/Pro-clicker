from time import sleep, localtime, strftime
import keyboard
from random import randint
from click.click_to_banana import click_to_banana
from click.find_icon import find_and_open, find_close

is_clicking = False
hours = 0


def clicking():
    global is_clicking
    is_clicking = not is_clicking
    if is_clicking:
        print("Now we are clicking"),
    else:
        print("Stop clicking")


keyboard.add_hotkey("ctrl+alt+b", lambda: clicking())
while True:
    if is_clicking:
        print(f"Hour: {hours} Time: {strftime("%H:%M:%S", localtime())}")
        if hours % 3 == 0 or hours % 17 == 0:
            print("We are in work")
            find_and_open()
            click_to_banana()
            find_close()
        sleep(randint(3600, 3650))
        hours += 1
    else:
        continue
