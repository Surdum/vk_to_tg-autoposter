import telebot
from autoposter import check_updates
from time import sleep, time, ctime



if __name__ == '__main__':
    while True:
        try:
            # none_stop - постоянная проверка
            # timeout - частота проверки в группе в сек (минимум 25)
            # max_post_size - максимальная длина поста в символах
            check_updates(none_stop=True, timeout=25, max_post_size=600)
        except Exception as e:
            print(ctime(time()), e)
        sleep(25)
