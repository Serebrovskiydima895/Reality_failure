import telebot
import os

BOT_TOKEN = os.getenv("TOKEN")
telebot = telebot.TeleBot(BOT_TOKEN)