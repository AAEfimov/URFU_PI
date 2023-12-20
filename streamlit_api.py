"""
streamlit_api.py
Streamlit based web interface
"""

__author__      = "UrFU team"
__copyright__   = "Copyright 2023, Planet Earth"

import io
import streamlit as sl
from PIL import Image
from project import *


def load_image():
    """
    Create filed on the web page to upload image
    """
    uploaded_file = sl.file_uploader(
            label='Выберите изобрадение')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        
        img = Image.open(io.BytesIO(image_data))
        img.save(uploaded_file.name)

        return  uploaded_file.name
    else:
        return None


    
sl.title('Генератор забавных картинок по описанию и фотографии')

img = load_image()

text = sl.text_area("Опишите, что должно произойти")
"""
Test area on the web page to input image describe
"""

def make_magic():
    """
    Button calback. Will check image and text. 
    Call main functional to generate image
    When image done, we put it on main page
    """
    if img and text:
        image_path, image_result = make_image(img, text)
        print("IMG_DONE")
        sl.image(image_result)

    else:
        sl.text("Пожалуйста, добавьте картинку и описание")


button = sl.button("make magic!", on_click=make_magic)
"""
Streamlit button.
after click, run calback and make_magic
"""


