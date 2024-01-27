import requests
import json
from settings import BASE_DJANGO_URL


def get_all_user_ids():
    """"Возвращает список всех пользователей бота"""
    url = f'{BASE_DJANGO_URL}botusers/'
    response = requests.get(url)
    telegram_ids = [el['user_id'] for el in response.json()]

    return telegram_ids


def add_new_bot_user(user_id):
    """"Добавляет нового пользователя в базу"""
    url = f'{BASE_DJANGO_URL}botusers/'
    data = {
        "user_id": user_id
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=json.dumps(data), headers=headers)


def add_film_to_django_db(title, year):
    """"Добавляет фильм в базу, возвращает ID фильма"""
    url = f'{BASE_DJANGO_URL}allfilms/'

    data = {
        "title": title,
        "year": year
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    response_json = response.json()
    return response_json['id']


def change_category_of_the_film(film_id, category=None):
    """"Меняет категорию фильма"""
    url = f'{BASE_DJANGO_URL}allfilms/{film_id}/'
    response = requests.get(url)
    response_json = response.json()
    response_json['category'] = category
    headers = {'Content-Type': 'application/json'}
    requests.put(url, data=json.dumps(response_json), headers=headers)


def get_list_of_all_films():
    """"Загружает список всех фильмов из базы для выявления новых"""
    url = f'{BASE_DJANGO_URL}allfilms/'
    response = requests.get(url)
    return response.json()


def show_list_of_requested_films(endpoint_url):
    """"Возвращает запрошенный список фильмов"""
    url = f'{BASE_DJANGO_URL}{endpoint_url}'
    list_of_films = []
    response = requests.get(url)
    response_json = response.json()
    for el in response_json:
        list_of_films.append({'title': el['title'], 'year': el['year']})
    result_string = "\n".join([f"<code>{film['title']}</code>, {film['year']}" for film in list_of_films])
    return result_string


def show_list_of_last_10_films():
    """"Возвращает список последних десяти фильмов"""
    url = f'{BASE_DJANGO_URL}lastfilms/'
    list_of_films = []
    response = requests.get(url)
    respons_json = response.json()
    results = respons_json['results']
    for el in results:
        list_of_films.append({'title': el['title'], 'year': el['year']})
    result_string = "\n".join([f"<code>{film['title']}</code>, {film['year']}" for film in list_of_films])
    return result_string
