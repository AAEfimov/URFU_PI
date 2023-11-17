import uuid
import os
from fastapi.responses import JSONResponse, FileResponse
from fastapi import FastAPI, Body, status
from bs4 import BeautifulSoup
from project import *

pe_urfu = FastAPI()

class pe_image():
    def __init__(self, pwd, text):
        self.pwd = pwd
        self.text = text
        self.img_id = str(uuid.uuid4())

img_list = []

def find_img(img_id):
    for i in img_list:
        if i.img_id == img_id:
            return i
    return None

@pe_urfu.get("/")
async def root():
    return FileResponse("public/index.html")

@pe_urfu.get("/api")
async def root_api():
    return JSONResponse({"message" : "Добро пожаловать в API для генератора изображений"})

@pe_urfu.get("/api/images/get/{img_id}")
async def api_image_get(img_id):

    fimg = find_img(img_id)
    if fimg == None:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content = {"message" : "Нет такого ихображения"}
                )
    else:
        return FileResponse(fimg.pwd)

@pe_urfu.get("/api/images")
async def api_get_all():
    return img_list

@pe_urfu.delete("/api/images/delete/{img_id}")
def delete_image(img_id):

    print("try to delete: ", img_id)
    cimg = find_img(img_id)
    if cimg == None:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content = {"message" : "Нет такого ихображения"}
                )

    img_list.remove(cimg)
    return cimg

@pe_urfu.post("/api/generate")
def generate_image(data  = Body()):

    # DBG ADD
    # peimg = pe_image("image.png", data['text'])
    # img_list.append(peimg)
    # return peimg

    if 'img' not in data or 'text' not in data:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={ "message": "Добавьте Текст и ссылку на изображение в формате {\"img\" : \"IMG_URL\", \"text\" : \"TEXT\"}" }
        )

    img = data["img"]
    text = data["text"]

    image_path, image_result = make_image(img, text)

    print(image_path)
    peimg = pe_image(image_path, text)

    img_list.append(peimg)

    return peimg



