from os import system
import multiprocessing
from settings import BOT_NOTIFIER
from bot_handler.main import bot_handler
from tracker.main import film_tracker

system("title " + f'Films Tracker')


def main():
    """"Запуск bot_handler и films_tracker"""
    try:
        p1 = multiprocessing.Process(target=bot_handler)
        p2 = multiprocessing.Process(target=film_tracker)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        BOT_NOTIFIER.polling(non_stop=True)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
