import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
def write_message(sender, message):
    authorize.method('messages.send', {'user_id': sender,
                                       'message': message,
                                       'random_id': get_random_id()})

def write_message_for_chat(sender, message):
    authorize.method('messages.send', {'chat_id': sender,
                                       'message': message,
                                       'random_id': get_random_id()})

def write_message_with_sticker(sender, sticker_id):
    authorize.method('messages.send', {'user_id': sender,
                                       'sticker_id': sticker_id,
                                       'random_id': get_random_id()})

token = "ec4e237351d28971b2fd592184f44692eed3a471416e0e0237e4b8a9bb5ef634ab40e95a668283ab2e9c8"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
list_of_users = []
write_message_for_chat(2000000179, "привет")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text
        sender = event.user_id
        if list_of_users.count(sender) == 0:
            list_of_users.append(sender)
            write_message(sender, "ты записан на рассылку")
        if received_message.lower() == "привет":
            write_message(sender, "y0")
            write_message_with_sticker(sender, 16947)
        elif received_message.lower() == "рассылка" and sender == 257857324:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    received_message = event.text
                    sender = event.user_id
                    for user in list_of_users:
                        write_message(user, received_message)
                break
        else:
            write_message(sender, "я тя не понимаю")