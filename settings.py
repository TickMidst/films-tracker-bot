from decouple import config
import os
import telebot

# Токен бота
BOT_TOKEN = config('BOT_TOKEN')

BOT_NOTIFIER = telebot.TeleBot(BOT_TOKEN)
BOT_LISTENER = telebot.TeleBot(BOT_TOKEN)

# Адрес вашего chromedriver
CHROME_DRIVER_ADRESS = "C:\\chromedriver.exe"

BASE_DIR = os.getcwd()
USER_PROFILE_DIR = os.path.join(BASE_DIR, "tracker\chrome_profile")

# Базовый URL на котором запущен проект Django
BASE_DJANGO_URL = 'http://127.0.0.1:8000/api/'
