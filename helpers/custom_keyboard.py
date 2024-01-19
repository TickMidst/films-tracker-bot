from telebot import types

class CustomKeyboard(types.InlineKeyboardMarkup):
    def __init__(self, film_id):
        buttons = [
            [types.InlineKeyboardButton("Добавить в категорию Плохие",
                                        callback_data=f"change_category_to_bad|{film_id}")],
            [types.InlineKeyboardButton("Добавить в категорию Хорошие",
                                        callback_data=f"change_category_to_good|{film_id}")],
            [types.InlineKeyboardButton("Убрать категорию",
                                        callback_data=f"change_category_to_null|{film_id}")],
        ]
        super().__init__()
        for button_row in buttons:
            self.row(*button_row)

        # Добавляем film_id как атрибут класса
        self.film_id = film_id
