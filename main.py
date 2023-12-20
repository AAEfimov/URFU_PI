"""
main.py
This is console example of our project
"""

__author__      = "UrFU team"
__copyright__   = "Copyright 2023, Planet Earth"

from  project import *

image_theme = 'village'
image_link = r'https://gdb.rferl.org/02be0000-0aff-0242-be17-08da2a16ec33_cx0_cy9_cw0_w1200_r1.jpg'

if __name__ == "__main__":
    image_path, image_result = make_image(image_link, image_theme)
    music_path, music_result = make_music(image_path)

    display(music_result)
    display(image_result)
