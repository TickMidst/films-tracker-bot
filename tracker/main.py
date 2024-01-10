from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import re
import subprocess
from datetime import datetime
from settings import DEBUGGER_ADDRESS, BOT_APP, CHROME_DRIVER_ADRESS
from helpers.link_decorator import LinkDecorator
from helpers.link_creator import LinkCreator
from helpers.custom_keyboard import CustomKeyboard
from api_requests.api_requests import add_film_to_django_db, get_list_of_all_films, get_all_user_ids

PATTERN = r"(.*)\s*\b(?:\s)?(?:\.|\(|\s)(202[1234])\b\s*(?:\)|\.|\s*)"

def open_distill(driver):
    driver.get('chrome-extension://inlikjemeeknofckkjolnjbpehgadgge/ui/inbox.html#/w/0/list/all/')
    sleep(5)


def send_message(text, film_id):
    telegram_ids = get_all_user_ids()
    for id in telegram_ids:
        try:
            with BOT_APP:
                keyboard = CustomKeyboard(film_id)
                BOT_APP.send_message(chat_id=id, text=text, reply_markup=keyboard, disable_web_page_preview=True)
        except Exception as e:
            print(e)


def film_tracker():
    shortcut_path = "Distill.lnk"
    command = f'start "" "{shortcut_path}"'

    # Открывает ярлык Chrome
    subprocess.run(command, shell=True)

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", DEBUGGER_ADDRESS)
    # Адрес chrome драйвера
    chrome_driver = CHROME_DRIVER_ADRESS
    service = Service(executable_path=chrome_driver)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Запускает расширение distill
    open_distill(driver)

    while True:
        response = get_list_of_all_films()
        # films_json = response['results']
        db_films_titles = [film['title'] for film in response]
        films_from_selenium = []

        # Ищет на странице все элементы с фильмами
        selenium_elements = driver.find_elements('xpath',
                                                 '//div[contains(@class, "xtd") and contains(@class, "xdata") and contains(@class, "xaction") and contains(@class, "cursor-pointer")]/span[normalize-space()]')
        for el in selenium_elements:
            match = re.search(PATTERN, el.text)
            try:
                new_film_title = LinkDecorator.replace_dots_with_spaces(match.group(1)).casefold()
                new_film_year = match.group(2)
                new_film_dict = {
                    'title': new_film_title,
                    'year': new_film_year
                }
                films_from_selenium.append(new_film_dict)
            except Exception as e:
                if AttributeError:
                    pass
                else:
                    print("Произошла ошибка:", e)

        new_films_titles_set = {film["title"] for film in films_from_selenium}
        # Находит названия фильмов которых нет в базе данных
        unique_titles = new_films_titles_set - set(db_films_titles)
        for unique_title in unique_titles:
            for film in films_from_selenium:
                if film['title'] == unique_title:
                    try:
                        imdb_link = LinkCreator.create_link_for_imdb(unique_title)
                        opensubs_link = LinkCreator.create_link_for_opensubs(unique_title)
                        new_film_year = str(film['year'])
                        copyable_title = f'"{unique_title}"'
                        text_to_send = (f'<code>{unique_title}</code> | {new_film_year}\n'
                                        f'<code>{copyable_title}</code> \n'
                                        f'{imdb_link} | {opensubs_link}')

                        # Вносит название фильма и год выпуска в БД и получает ID
                        film_id = add_film_to_django_db(unique_title, str(new_film_year))

                        # Отправляет данные с помощью Telegram бота
                        send_message(text_to_send, film_id)
                        current_time = datetime.now().time()
                        current_time_str = current_time.strftime("%H:%M:%S")
                        print('Добавил ', unique_title, new_film_year)
                        print('время:', current_time_str)
                        print('')
                        print('')
                        break
                    except Exception as e:
                        print(e)
                        break
        sleep(20)
