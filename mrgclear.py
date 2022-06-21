import telebot
import random
import logging
from telebot import types

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot("5345165100:AAF04G_rkh_uoxECYrTaOw_nTwV8PczpfX4", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_text(message):
    with open('tq.txt') as f:
        lines = f.readlines()
    try:
        with open("tq.txt", "a+") as file_object:
            print(message.text)
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            file_object.write(message.text)
    except:
        pass

bot.polling()
