from settings import BOT_2
from api_requests.api_requests import change_category_of_the_film, show_list_of_requested_films, \
    show_list_of_last_10_films, add_new_bot_user



def bot_handler():
    # Команды боту

    # Получает id пользователя и сохраняет его в БД
    @BOT_2.message_handler(commands = ["start"])
    def a(message):
        user_id = message.from_user.id
        add_new_bot_user(user_id)
    
    @BOT_2.message_handler(commands = ["show_all"])
    def a(message):
        raw_list = show_list_of_requested_films('allfilms/')
        BOT_2.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_2.message_handler(commands = ["show_last_10"])
    def a(message):
        raw_list = show_list_of_last_10_films()
        BOT_2.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_2.message_handler(commands = ["show_good"])
    def a(message):
        print('Жопа')
        raw_list = show_list_of_requested_films('goodfilms/')
        BOT_2.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_2.message_handler(commands = ["show_bad"])
    def a(message):
        raw_list = show_list_of_requested_films('badfilms/')
        BOT_2.reply_to(message, raw_list, parse_mode='HTML')

    @BOT_2.callback_query_handler(lambda query: query.data.startswith('change_category_to_bad'))
    def a(callback_query):
        print(callback_query.data)
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id, 1)
        BOT_2.answer_callback_query(callback_query.id, text='Категория изменена на "Плохая"')

    @BOT_2.callback_query_handler(lambda query: query.data.startswith('change_category_to_good'))
    def a(callback_query):
        print(callback_query.data)
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id, 2)
        BOT_2.answer_callback_query(callback_query.id, text='Категория изменена на "Хорошая"')

    @BOT_2.callback_query_handler(lambda query: query.data.startswith('change_category_to_null'))
    def a(callback_query):
        print(callback_query.data)
        data = callback_query.data.split("|")
        film_id = data[1]
        change_category_of_the_film(film_id)
        BOT_2.answer_callback_query(callback_query.id, text='Категория убрана')

    BOT_2.polling(none_stop=True)