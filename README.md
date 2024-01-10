# Films-tracker-bot

Работает только на Windows

Как пользоваться?
    1. клонировать себе на ПК
    1. установить зависимости виртуального окружения командной pipenv install
    2. Скачать chromedriver отсюда: https://googlechromelabs.github.io/chrome-for-testing/ (выбрать подходящую версию)
    3. Положить его в корень диска C, или в другую директорию (но тогда надо поменять адрес в CHROME_DRIVER_ADRESS)
    4. Установить обычный google chrome, создать ярлык, назвать его "Distill.lnk" и положить в корневую папку этого проекта
    5. Создать бота, написав https://t.me/BotFather команду /newbot
    6. Вставить токен бота в перменную BOT_TOKEN в settings.py
    7. Запустить сервер Django (https://github.com/TickMidst/films-tracker-django)