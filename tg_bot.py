import os
import telebot
import requests
import random
from PIL import Image
from gtts import gTTS
from gradio_client import Client
from project import *

def say_it(text, chat_id):
      sound_file = f'output_{str(chat_id)}.wav'
      tts = gTTS(text, lang="en", tld='com.mx')
      tts.save(sound_file)
      return sound_file

def prepare_image(image_file, text, user_id):

    image = Image.open(image_file).convert('RGB')
    image_name = f'initial_{user_id}.jpg'
    image.save(image_name)

    return make_image(image_file, text)

def prepare_music(image_file):
    image = Image.open(image_file).convert('RGB')
    image_name = f'initial_{user_id}.jpg'
    image.save(image_name)

    return make_music(image_file)

users_dict_text = {}
users_dict_pic = {}

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

def generate_all(message, img_file_name, text):
    try:
        chat_id = message.chat.id
        ret_file, img_result = prepare_image(img_file_name, text, message.from_user.id)
        img_ret = open(ret_file, "rb")
        bot.send_photo(chat_id, img_ret)
    except ValueError:
        print("Error generation")
        bot.reply_to(message, "Error, can't generate")


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    global users_dict
    users_dict_text[message.from_user.id] = message.text

    if message.from_user.id in users_dict_pic:
        generate_all(message, users_dict_pic[message.from_user.id], users_dict_text[message.from_user.id])
        del(users_dict_pic[message.from_user.id])
        del(users_dict_text[message.from_user.id])
    else:
        bot.reply_to(message, f"Text to Generation: {message.text} Now upload picture")

# Handles all sent documents and audio files
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    fileID = bot.get_file(message.photo[-1].file_id)
    print(f"FILE_ID {fileID}")

    downloaded_file = bot.download_file(fileID.file_path)
    img_file_name = f'photo{message.chat.id}.jpg'

    with open(img_file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    users_dict_pic[message.from_user.id] = img_file_name

    if message.from_user.id in users_dict_text:
        generate_all(message, users_dict_pic[message.from_user.id], users_dict_text[message.from_user.id])
        del(users_dict_pic[message.from_user.id])
        del(users_dict_text[message.from_user.id])
    else:
        bot.reply_to(message, f"Image added, Now add text")

bot.infinity_polling()
