from gradio_client import Client
import random
from PIL import Image
from IPython.display import Audio
import os
import requests
import re
from bs4 import BeautifulSoup

image_model = 'https://mikonvergence-theatron.hf.space/'
music_model = 'https://fffiloni-image-to-musicgen.hf.space/'

def find_API(link):
	response = requests.get(link + '?view=api')
	bs = BeautifulSoup(response.text, "lxml")
	API = bs.find_all('script')
	regex = re.compile('--replicas/\w{1,}')
	return link + regex.search(API[1].text).group()

def make_image(image_link, image_theme):
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
  image_path = tuple(os.walk(result))[1][0] + '/image.png'
  image_result = Image.open(image_path)
  return image_path, image_result


def make_music(image_path):
  API_link = find_API(music_model)
  client = Client(API_link)
  music_path = client.predict(
		image_path,	# str (filepath on your computer (or URL) of image) in 'Input Image' Image component
		"",	# str (filepath on your computer (or URL) of file) in 'Melody Condition (optional)' Audio component
		30,	# int | float (numeric value between 1 and 30) in 'Duration' Slider component
		fn_index=0
  )
  music_result = Audio(music_path, autoplay = True)
  return music_path, music_result
