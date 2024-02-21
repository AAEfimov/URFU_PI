"""
fastapi_ex.py
Fastapi functions
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2023, Planet Earth"

import uuid
import os
from fastapi.responses import JSONResponse, FileResponse
from fastapi import FastAPI, Body, status
from bs4 import BeautifulSoup
from project import *

pe_urfu = FastAPI()


class pe_image:
    """
    Class for accumulate generated image information and provide access to new images
    """

    def __init__(self, pwd, text, uid=None):
        # Initialize the class with the provided parameters: pwd (password), text, and optional uid (unique identifier)
        self.pwd = pwd  # Set the pwd attribute to the provided password
        self.text = text  # Set the text attribute to the provided text
        if uid == None:  # Check if the uid parameter is not provided
            # Generate a new unique identifier using uuid if uid is not provided
            self.img_id = str(uuid.uuid4())
        else:
            # Use the provided uid as the unique identifier
            self.img_id = str(uid)


img_list = [pe_image("Img/result.png", "On the moon", "1")]


def find_img(img_id):
    """
    Find image by id in saved images
    img_id -- uuid for generated image
    """
    for i in img_list:
        if i.img_id == img_id:
            return i
    return None


@pe_urfu.get("/")
async def root():
    """
    Fast api root page
    """
    return FileResponse("public/index.html")


@pe_urfu.get("/api")
async def root_api():
    """
    Fast api Hello api page. GET REQUEST
    """
    return JSONResponse(
        {"message": "Добро пожаловать в API для генератора изображений"}
    )


@pe_urfu.get("/api/images/get/{img_id}")
async def api_image_get(img_id):
    """
    Fast api - get image by ID. GET REQUEST
    img_id - UUID of image
    """
    fimg = find_img(img_id)
    if fimg == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Нет такого ихображения"},
        )
    else:
        return FileResponse(fimg.pwd)


@pe_urfu.get("/api/images")
async def api_get_all():
    """
    Fast api - get all image list. GET REQUEST
    """
    return img_list


@pe_urfu.delete("/api/images/delete/{img_id}")
def delete_image(img_id):
    """
    Fast api - delete image by UUID. DELETE REQUEST
    img_id - image UUID
    """
    print("try to delete: ", img_id)
    cimg = find_img(img_id)
    if cimg == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Нет такого ихображения"},
        )

    img_list.remove(cimg)
    return cimg


@pe_urfu.post("/api/generate")
def generate_image(data=Body()):
    """
    Fast api - generate image. POST REQUSET
    data - dict with data["img"] and data["text"] fields
    """
    # DBG ADD
    # peimg = pe_image("image.png", data['text'])
    # img_list.append(peimg)
    # return peimg

    if "img" not in data or "text" not in data:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": 'Добавьте Текст и ссылку на изображение в формате {"img" : "IMG_URL", "text" : "TEXT"}'
            },
        )

    img = data["img"]
    text = data["text"]

    image_path, image_result = make_image(img, text)

    print(image_path)
    peimg = pe_image(image_path, text)

    img_list.append(peimg)

    return peimg
