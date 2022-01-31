import vk_api
from vk_api import VkUpload
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from tok import tok
import time

def dialog_sender(sender, message):
    authorize.method('messages.send', {'user_id': sender,
                                       'message': message,
                                       'random_id': get_random_id()})

def dialog_sender_with_keyboard(sender, message):
    authorize.method('messages.send', {'user_id': sender,
                                       'message': message,
                                       'random_id': get_random_id(),
                                       'keyboard': keyboard.get_keyboard()})

def chat_sender(sender, message):
    authorize.method('messages.send', {'chat_id': sender,
                                       'message': message,
                                       'random_id': get_random_id()})

def chat_sender_with_sticker(sender, sticker_id):
    authorize.method('messages.send', {'chat_id': sender,
                                       'sticker_id': sticker_id,
                                       'random_id': get_random_id()})

token = tok
authorize = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(authorize, group_id=209649159)
list_of_chats = []
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.message.get('text') != "":
        received_message = event.message.get('text')
        if event.from_chat:
            sender = event.chat_id
            if list_of_chats.count(sender) == 0:
                list_of_chats.append(sender)
                chat_sender_with_sticker(sender, 62823)
        else:
            sender = event.message.get('from_id')
            if received_message.lower() == "рассылка" and sender == 257857324:
                dialog_sender(sender, "Введи сообщение для рассылки")
                for event in longpoll.listen():
                   # dialog_sender(sender, "зашел в цикл")
                    mark = False
                    mark2 = False
                    if event.type == VkBotEventType.MESSAGE_NEW and event.message.get('text') != "":
                        received_message = event.message.get('text')
                        sender = event.message.get('from_id')

                        keyboard = VkKeyboard(one_time=True)
                        keyboard.add_button("Всё верно", color = VkKeyboardColor.POSITIVE)
                        keyboard.add_button("Исправить", color = VkKeyboardColor.NEGATIVE)
                        saved_message = received_message
                        dialog_sender_with_keyboard(sender, "Сообщение без ошибок?")

                        for event in longpoll.listen():
                            if event.type == VkBotEventType.MESSAGE_NEW:
                                received_message = event.message.get('text')
                                sender = event.message.get('from_id')
                                if received_message == "Всё верно":
                                    start_time = time.time()
                                    for chat in list_of_chats:
                                        chat_sender(chat, saved_message)
                                    end_time = time.time()
                                    dialog_sender(sender, f"Рассылка завершена за {round(end_time - start_time, 1)} сек")
                                    mark2 = True
                                    break
                                else:
                                    mark = True
                                    dialog_sender(sender, "Введи исправленное сообщение")
                                    break
                    if(mark):
                        continue
                   # dialog_sender(sender, "вышел из цикла")
                    if(mark2):
                       break


