from pyrogram import Client
from decouple import config


# Токен бота
BOT_TOKEN = config('BOT_TOKEN')

# адрес вашего chromedriver
CHROME_DRIVER_ADRESS = "C:\\chromedriver.exe"

# Базовый URL на котором запущен проект Django
BASE_URL = 'http://127.0.0.1:8000/api/'

BOT_HANDLER_APP = Client("bot_handler_account", bot_token=BOT_TOKEN)
BOT_APP = Client("bot_account", bot_token=BOT_TOKEN)

# Адрес по которому открывается chrome distill
DEBUGGER_ADDRESS = '127.0.0.1:9222'
