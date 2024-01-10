from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CustomKeyboard(InlineKeyboardMarkup):
    def __init__(self, film_id):
        self.film_id = film_id
        buttons = [
            [InlineKeyboardButton("Добавить в категорию Плохие",
                                  callback_data="change_category_to_bad|{}".format(str(film_id)))],
            [InlineKeyboardButton("Добавить в категорию Хорошие",
                                  callback_data="change_category_to_good|{}".format(str(film_id)))],
            [InlineKeyboardButton("Убрать категорию",
                                  callback_data="change_category_to_null|{}".format(str(film_id)))]
        ]
        super().__init__(buttons)
