# Films-Tracker-Bot

## Возможности проекта:
Данная программа позволяет отслеживать фильмы, которые появляются на торрент трекерах и сайтах с релизами. При обнаружении фильма его название сверяется с [базой данный](https://github.com/TickMidst/films-tracker-django) и если его там нет, он вносится в базу данных и высылается пользователям бота в следующем виде:

![Образец](https://sun9-12.userapi.com/impf/L6dtY_nAbwPS9YQYoA-p_evEtKRt_ErXDO6tLw/PR_mC5BMyRg.jpg?size=895x230&quality=96&sign=2745b9ab6a47615ce68427a8a46c5521&type=album)

С помощью кнопок в боте фильм можно добавить в одну из двух категорий, либо убрать из них. 

Таким образом данная программа позволяет получать уведомления о выходе исключительно новых фильмов, не получая уведомления о повторных релизах (коих очень много). Фильмы берутся только 2021-2024 годов выпуска.

## Требования:

- [Сервер Django](https://github.com/TickMidst/films-tracker-django)
- Windows
- Chromedriver
- Google Chrome
- Аккаунт Telegram

## Установка:
1. Клонировать репозиторий на свой ПК.
2. Установить зависимости виртуального окружения с помощью команды `pipenv install`.
3. [Скачать подходящую версию Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/). Они находятся в разделе `stable` и называются `chromedriver`. ([Версия для win64](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip)).
4. поместить `chromedriver` и `LICENSE.chromedriver` в корень диска C или в другую директорию (но при этом надо изменить адрес в переменной `CHROME_DRIVER_ADDRESS`).
5. При необходимости установить стандартный `Google Chrome`
6. Создать ярлык Chrome, переименовать в `Distill.lnk` и поместить в корневую папку проекта.
7. Создать бота, отправив команду `/newbot` [BotFather](https://t.me/BotFather).
8. Указать токен бота в переменной `BOT_TOKEN` в файле `settings.py`:
   
   ![токен](https://sun9-30.userapi.com/impf/kgJZIX5NUy0SyZRoheP8CXXqd603PxkSsie-VQ/xJKBSKL1TIQ.jpg?size=608x88&quality=96&sign=2804d51d9172cf4312349a6107e9c175&type=album)

## Первый запуск:
1. Запустить [сервер Django](https://github.com/TickMidst/films-tracker-django).
2. Запустить бота с помощью команды `python main.py`
3. Откроется окно установки расширения `distill-web-monitor`
4. Нажать кнопку `установить`
5. После установки `перейти к Watchlist`
      
   ![watchlist](https://sun9-34.userapi.com/impf/j2er5pg8YB2Yi7DnBS7_OqhHy4qORO3xVdJw7A/ASYSbHzsd4c.jpg?size=507x249&quality=95&sign=2a4ebe46b91af9db16acb1efdd7fdde5&type=album)
6. `import` -> `json`   
   ![watchlist](https://sun9-50.userapi.com/impf/a9twfiD4SrSvGUEuLtSomHGEhAeY_FGtJdF_5g/VOLQCQ1GC5s.jpg?size=641x399&quality=96&sign=3cf58432cd1ec27225c4b844b769229e&type=album)
7. `select json`, выбрать файл `distill_settings.json` из папки `tracker` проекта
   ![watchlist](https://sun9-40.userapi.com/impf/zPB1kOGIk99jQwHoBwOrsjicGVxa2TB8gFps4w/I8A4xlUiknQ.jpg?size=602x300&quality=95&sign=2ae7e2e074558701506afecf6292bb18&type=album)
8. `next`, `import`
   ![watchlist](https://sun9-58.userapi.com/impf/37dunMZ7Asl5OVGegLIOfjmJnIfYFvfhvVSPiQ/yCa-FK0o0Jg.jpg?size=570x166&quality=96&sign=f44f41675003993c2d5664b09c5e603d&type=album)
   ![watchlist](https://sun9-68.userapi.com/impf/iuRzk7Ka4Dg9zwLOYKbcuzeFvghVsVTEmR1KtA/mNPruvvPHH0.jpg?size=386x166&quality=95&sign=4d7b8043cae16cb982e2cce8885f4428&type=album)
9.   отправить боту команду `/start` чтобы подписаться на получение новых фильмов
10. Закрыть окно `Selenium браузера`
11. Завершить выполнение кода
12. Добавить необходимые команды боту:
   - В настройках бота нажать `"управление ботом"`
   - Затем `"изменить команды"`
   - Отправить следующий текст:
```
show_all - показать все фильмы
show_last_10 - показать последние десять фильмов
show_good - показать хорошие фильмы
show_bad - показать плохие фильмы
```

## Как пользоваться ботом:

1. Запустить [сервер Django](https://github.com/TickMidst/films-tracker-django).
2. При обнаружении нового фильма в телеграм бот придёт сообщение в указанном в начале виде.
3. Для добавления фильма в категории необходимо воспользоваться кнопками которые приходят вместе с обнаруженным фильмом.
4. Для того чтобы увидеть фильмы из определённых категорий, все фильмы или последние десять найденных фильмов нужно воспользоваться командами бота.
      
   ![watchlist](https://sun9-48.userapi.com/impf/KSdf-0GJWwkbE5cC1v8Lj33cSRCsBzRKVFZOkg/UfxNq-o1OUg.jpg?size=688x278&quality=95&sign=59ced185fad052885794c4a713d74dd5&type=album)