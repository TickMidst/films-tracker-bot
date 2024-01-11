# Films-tracker-bot

## Требования:

- Windows
- Chromedriver
- Google Chrome
- Аккаунт Telegram

## Как пользоваться:

1. Клонировать репозиторий на свой компьютер.
2. Установить зависимости виртуального окружения с помощью команды `pipenv install`.
3. [Скачать Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/) (выбрать подходящую версию) и поместить в корень диска C или в другую директорию (не забудьте изменить адрес в переменной `CHROME_DRIVER_ADDRESS`).
4. Установить обычный Google Chrome, создать ярлык, назвать его "Distill.lnk" и поместить в корневую папку проекта.
5. Создать бота, отправив команду `/newbot` [BotFather](https://t.me/BotFather).
6. Указать токен бота (в виде строки) в переменной `BOT_TOKEN` в файле `settings.py`.
7. Запустить сервер Django ([ссылка на репозиторий](https://github.com/TickMidst/films-tracker-django)).
