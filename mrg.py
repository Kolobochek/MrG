import telebot
import random
import logging
from telebot import types

list1 = ["Пизда", "Хуй на"]

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
    if message.text.lower() == "да" or message.text.lower() == "@mrgshit_bot да":
        bot.reply_to(message, random.choice(list1))
    elif "твоя" in message.text.lower() and "мама" in message.text.lower():
        bot.reply_to(message, "Польская кошкодевочка с миской риса")
    elif "твой" in message.text.lower() and "папа" in message.text.lower():
        bot.reply_to(message, "Гений, миллиардер, плейбой, филантроп")
    elif message.text.lower() == "асу" or message.text.lower() == "@mrgshit_bot асу":
        bot.reply_to(message, "Пов: ввели санкции на буквы Ж Д А Ю")
    elif message.text.lower() == 'пизда':
        bot.reply_to(message, "Это моя фраза, чмо")
    elif message.text.lower() == 'хуй на':
        bot.reply_to(message, "Соси два")
    elif "алина" in message.text.lower():
        bot.reply_to(message, "Алина шлюха")
    elif "путин" in message.text.lower():
        bot.reply_to(message, "Путин хуйло")
    else:
        if random.randint(0,100) < 15 or "@mrgshit_bot" in message.text.lower():
            try:
                bot.reply_to(message, random.choice(lines))
            except:
                pass
    
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    bot.reply_to(message, "2")
bot.polling()