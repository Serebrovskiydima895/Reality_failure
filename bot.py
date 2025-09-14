from os import linesep
from plistlib import loads
from unittest.mock import sentinel

import telebot
import os
from dotenv import load_dotenv
import function

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
telebot = telebot.TeleBot(BOT_TOKEN)
information_user = {}
admin = []

@telebot.message_handler(commands=["start"])
def start(message):
    telebot.send_message(message.chat.id, "Привет! От тебя кое-какие данные")



@telebot.message_handler(commands=["text"])
def regestraion(message):
    telebot.send_message(message.chat.id, "Напиши свой ник!")
    mess = message.text
    if function.check_nik(mess):
        information_user["Имя"] = mess
    else:
        telebot.send_message(message.chat.id, "Ты не ввел ник! Напиши заново!")
        mess = message.text


telebot.polling()