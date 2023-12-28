"""
project.py
main functional to communication with ML model
"""

__author__      = "UrFU team"
__copyright__   = "Copyright 2023, Planet Earth"

from gradio_client import Client
import random
from PIL import Image
from IPython.display import Audio
import os
import requests
import re

image_model = 'https://mikonvergence-theatron.hf.space/'

def find_API(link):
    """
    Find API link from web page
    link -- URL address uf model
    """
    response = requests.get(link + '?view=api')
    regex = re.compile('--replicas/\w{1,}')
    return link + regex.search(response.text).group()

def make_image(image_link, image_theme):
    """
    Send request to ML model placed on hugging face
    and get generated image
    image_link -- link for sorce image
    image_theme -- discribe what we shoul do
    """
    API_link = find_API(image_model)
    client = Client(API_link)
    result = client.predict(
	  image_link,	# str (filepath on your computer (or URL) of image) in 'Webcam' Image component
	  image_link,	# str (filepath on your computer (or URL) of image) in 'Image Upload' Image component
	  image_theme,	# str  in 'Prompt:' Textbox component
	  "bad anatomy, extra limbs, connected limbs, fused limbs, deformed hands, mutant",	# str  in 'Negative Prompt: Avoid these features in the image...' Textbox component
	  100,	# int | float (numeric value between 1 and 100) in 'Steps' Slider component
		random.randint(-1, 2147483647),	# int | float (numeric value between -1 and 2147483647) in 'Seed' Slider component
		True,	# bool  in 'Preserve Resolution' Checkbox component
		fn_index=1
  )
    image_path = tuple(os.walk(result))[1][0] + '/image.png'	# Get the path to the image
    image_result = Image.open(image_path)	# Opening an image
    return image_path, image_result	# Return the path to the image and the image itself

