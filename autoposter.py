import requests
import telebot
from time import sleep
import json
from const import *

post_size = 0
autoposter = telebot.TeleBot(BOT_TOKEN)



def send_post(post):
    text: str
    global post_size
    from_id = post["from_id"]
    id_ = post["id"]
    if 'copy_history' in post:                            # переход к репосту
        post = post['copy_history'][-1]
    if len(post['text']) > post_size:
        text = post['text'][0:post['text'].rfind('.', 0, post_size) + 1]
    else:
        text = post['text']
    text += f'..\n[Перейти к статье](http://vk.com/{GROUP_NAME}?w=wall{from_id}_{id_})'
    if text.find('\n') <= 100:
        text = '*' + text[0:text.find('\n')] + '*' + text[text.find('\n'):]
    print(text)
    for channel in CHANNELS:
        if text:
            try:
                autoposter.send_message(channel, text, parse_mode='Markdown')
            except Exception:
                pass


def check():
    posts = requests.get(URL_VK).json()
    posted_ids = json.loads(open('posts.json', 'r').read())
    last = []
    for i in range(4, -1, -1):
        checked_post = posts['response']['items'][i]
        if checked_post['id'] > posted_ids[-1]['id']:
            send_post(checked_post)
            last.append({'id': checked_post['id']})
            json.dump(last, open('posts.json', 'w'))


def check_updates(none_stop=False, timeout=10, max_post_size=500):
    global post_size
    post_size = max_post_size
    check()
    while none_stop:
        sleep(timeout)
        check()


if __name__ == "__main__":
    print('Это не main')