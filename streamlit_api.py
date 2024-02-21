"""
streamlit_api.py
Streamlit based web interface
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2023, Planet Earth"

import io

import streamlit as sl
from PIL import Image

from project import *

# from tqdm import tqdm
# import time


def load_image():
    """
    Create filed on the web page to upload image
    """
    uploaded_file = sl.file_uploader(label="Выберите изобрадение")
    # Check if an image file is uploaded
    if uploaded_file is not None:
        # Get the image data
        image_data = uploaded_file.getvalue()

        # Open the image using the BytesIO and Image modules
        img = Image.open(io.BytesIO(image_data))
        # Save the uploaded image with its original name
        img.save(uploaded_file.name)

        # Return the name of the uploaded image file
        return uploaded_file.name
    else:
        # If no image is uploaded, return None
        return None


sl.title("Генератор забавных картинок по описанию и фотографии")

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
"""
# Information about the generation process
def generate_images(image_list):
    results = []
    for image in tqdm(image_list, desc='Processing images', unit='image'):
        # Code for image processing
        time.sleep(0.1)  # To demonstrate the delay in processing each image
        results.append(image)  # Here you can add the processed image to the list of results
    return results

# Usage example
image_list = [image1, image2, image3]  # Replace with your list of images
processed_images = generate_images(image_list)
"""
