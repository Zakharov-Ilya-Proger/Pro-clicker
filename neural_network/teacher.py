from PIL import Image
from art import tprint
from random import shuffle, choice
from icecream import ic


def create_wallpaper(target_icon: Image,
                     grade: int = 1,
                     icon_size: tuple = (89, 89),
                     grid_params: tuple = (9, 19)
                     ):

    grid_rows, grid_cols = grid_params

    wallpaper = Image.open("../photos/wallpaper.png")
    icons = [Image.open(f"../photos/wrong_icon_{i % 8}.png") for i in range(1, round(7 * grade)) if i % 8 != 0]

    shuffle(icons)

    desktop_width, desktop_height = wallpaper.size

    flat_coordinates = [(desktop_width // grid_cols * j, desktop_height // grid_rows * i)
                        for i in range(grid_rows)
                        for j in range(grid_cols)]
    ic(len(flat_coordinates))
    icons = icons[:len(flat_coordinates) - 1]
    icons.append(target_icon)

    target_icon_center = tuple()

    for i, icon in enumerate(icons):

        x, y = choice(flat_coordinates)
        flat_coordinates.remove((x, y))

        wallpaper.paste(icon, (x, y), icon.convert("RGBA"))

        if i == len(icons) - 1:
            target_icon_center = (x + icon_size[0] // 2, y + icon_size[1] // 2)

    wallpaper.save('../photos/desktop_with_icons.png')
    return wallpaper, target_icon_center


if __name__ == '__main__':
    tprint("---In Work---")
    create_wallpaper(Image.open("../photos/target_icon.png"), grade=100)
    tprint("     ---Finish---")
    