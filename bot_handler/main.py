from settings import BOT_HANDLER_APP
from pyrogram import filters
from helpers.custom_keyboard import CustomKeyboard
from api_requests.api_requests import change_category_of_the_film, show_list_of_requested_films, \
    show_list_of_last_10_films, add_new_bot_user


def bot_handler():
    # Команды боту

    # Получает id пользователя и сохраняет его в БД
    @BOT_HANDLER_APP.on_message(filters.command("start"))
    def a(client, message):
        user_id = message.from_user.id
        add_new_bot_user(user_id)
    
    @BOT_HANDLER_APP.on_message(filters.command("show_all"))
    def a(client, message):
        raw_list = show_list_of_requested_films('allfilms/')
        message.reply(raw_list)

    @BOT_HANDLER_APP.on_message(filters.command("show_last_10"))
    def a(client, message):
        raw_list = show_list_of_last_10_films()
        message.reply(raw_list)

    @BOT_HANDLER_APP.on_message(filters.command("show_good"))
    def a(client, message):
        raw_list = show_list_of_requested_films('goodfilms/')
        message.reply(raw_list)

    @BOT_HANDLER_APP.on_message(filters.command("show_bad"))
    def a(client, message):
        raw_list = show_list_of_requested_films('badfilms/')
        message.reply(raw_list)

    @BOT_HANDLER_APP.on_callback_query(filters.regex(r'^change_category_to_bad\|'))
    def a(client, callback_query):
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id, 1)
        callback_query.answer(format('Категория изменена на "Плохая"'))

    @BOT_HANDLER_APP.on_callback_query(filters.regex(r'^change_category_to_good\|'))
    def a(client, callback_query):
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id, 2)
        callback_query.answer(format('Категория изменена на "Хорошая"'))

    @BOT_HANDLER_APP.on_callback_query(filters.regex(r'^change_category_to_null\|'))
    def a(client, callback_query):
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id)
        callback_query.answer(format('Категория убрана'))

    BOT_HANDLER_APP.run()
