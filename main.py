from  project import *

image_theme = 'village'
image_link = r'https://gdb.rferl.org/02be0000-0aff-0242-be17-08da2a16ec33_cx0_cy9_cw0_w1200_r1.jpg'

image_path, image_result = make_image(image_link, image_theme)
music_path, music_result = make_music(image_path)

display(music_result)
display(image_result)
