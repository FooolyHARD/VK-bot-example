import vk_api
import requests
from vk_api.longpoll import VkLongPoll,VkEventType
token_file = open('tkn.txt', 'r')
token = token_file.readline()
session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            if event.text == "ты еблан" or event.text=="я еблан":
                vk.messages.send(user_id = event.user_id, message = "da", random_id = 0)
                print(event.user_id)
            else:
                vk.messages.send(user_id = event.user_id, message = str(event.datetime)+" пошел нахуй", random_id = 0)
        elif event.from_chat:
            vk.messages.send(
                user_id = event.user_id,
                message = 'Нет'

                )
