from settings import BOT_LISTENER
from api_requests.api_requests import change_category_of_the_film, show_list_of_requested_films, \
    show_list_of_last_10_films, add_new_bot_user, get_all_user_ids


def bot_handler():
    # Команды боту
    def notificate_list_is_empty(message):
        return BOT_LISTENER.reply_to(message, 'Список пуст')

    # Получает id пользователя и сохраняет его в БД
    @BOT_LISTENER.message_handler(commands=["start"])
    def a(message):
        user_id = message.from_user.id
        telegram_ids = get_all_user_ids()
        if user_id in telegram_ids:
            BOT_LISTENER.reply_to(message, 'Вы уже внесены в базу рассылки')     
        else:
            add_new_bot_user(user_id)
            BOT_LISTENER.reply_to(message, 'Вы были внесены в базу рассылки') 

    @BOT_LISTENER.message_handler(commands=["show_all"])
    def a(message):
        raw_list = show_list_of_requested_films('allfilms/')
        if raw_list == '':
            return notificate_list_is_empty(message)
        BOT_LISTENER.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_LISTENER.message_handler(commands=["show_last_10"])
    def a(message):
        raw_list = show_list_of_last_10_films()
        if raw_list == '':
            return notificate_list_is_empty(message)
        BOT_LISTENER.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_LISTENER.message_handler(commands=["show_good"])
    def a(message):
        raw_list = show_list_of_requested_films('goodfilms/')
        if raw_list == '':
            return notificate_list_is_empty(message)
        BOT_LISTENER.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_LISTENER.message_handler(commands=["show_bad"])
    def a(message):
        raw_list = show_list_of_requested_films('badfilms/')
        if raw_list == '':
            return notificate_list_is_empty(message)
        BOT_LISTENER.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_LISTENER.callback_query_handler(lambda query: query.data.startswith('change_category_to_bad'))
    def a(callback_query):
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id, 1)
        BOT_LISTENER.answer_callback_query(callback_query.id, text='Категория изменена на "Плохая"')

    @BOT_LISTENER.callback_query_handler(lambda query: query.data.startswith('change_category_to_good'))
    def a(callback_query):
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id, 2)
        BOT_LISTENER.answer_callback_query(callback_query.id, text='Категория изменена на "Хорошая"')

    @BOT_LISTENER.callback_query_handler(lambda query: query.data.startswith('change_category_to_null'))
    def a(callback_query):
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id)
        BOT_LISTENER.answer_callback_query(callback_query.id, text='Категория убрана')

    BOT_LISTENER.polling(none_stop=True)
