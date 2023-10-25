import io

import streamlit as sl
from PIL import Image
from project import *


def load_image():
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

def make_magic():
    if img and text:
        image_path, image_result = make_image(img, text)
        print("IMG_DONE")
        sl.image(image_result)

    else:
        sl.text("Пожалуйста, добавьте картинку и описание")


button = sl.button("make magic!", on_click=make_magic)



