from pyrogram import Client
from decouple import config


# Токен бота
BOT_TOKEN = config('BOT_TOKEN')

# Адрес вашего chromedriver
CHROME_DRIVER_ADRESS = "C:\\chromedriver.exe"

# Адрес профиля с установленным расширением Distill
USER_DATA_DIR = "C:\\selenum\\ChromeProfile"

# Базовый URL на котором запущен проект Django
BASE_DJANGO_URL = 'http://127.0.0.1:8000/api/'

BOT_HANDLER_APP = Client("bot_handler_account", bot_token=BOT_TOKEN)
BOT_APP = Client("bot_account", bot_token=BOT_TOKEN)
