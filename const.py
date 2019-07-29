# GROUP_NAME - id группы в адр строке
GROUP_NAME = ''
# ACCESS_TOKEN - токен, полученный от приложения; scope=wall,offline
ACCESS_TOKEN = ''
BOT_TOKEN = ''
# POST_COUNT - количество проверяемых постов. Из 5 пересылаются только новые.
POST_COUNT = 5
URL_VK = f'https://api.vk.com/method/wall.get?domain={GROUP_NAME}&count={POST_COUNT}&v=5.74&filter=owner' \
         f'&access_token={ACCESS_TOKEN}'

# id каналов для рассылки
CHANNELS = [0, 1]
