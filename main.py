import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Первая кнопка', color=VkKeyboardColor.POSITIVE)    #DEFAULT - Серый, POSITIVE - Зелёный, NEGATIVE - красный, PRIMARY - синий
keyboard.add_line()
keyboard.add_button('Вторая кнопка', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('Третья кнопка', color=VkKeyboardColor.SECONDARY)
keyboard.add_line()
keyboard.add_openlink_button('Кнопка ссылки', link="https://vk.com/")
def write_message(sender, message):
    authorize.method('messages.send', {'user_id': sender,
                                       'message': message,
                                       'random_id': get_random_id(),
                                       'attachment': ','.join(attachments),
                                       'keyboard': keyboard.get_keyboard()})

token = "29cb9d5b2c75f99cdcfa25a5a8677a0b2cbbbbff6be36b60b35b66f910f0009788bc0159d669a39fa3aed"
image = "D:/Adobe Photoshop/Adobe Photoshop/Ya/Изображение.jpg"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
upload = VkUpload(authorize)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text
        sender = event.user_id
        attachments = []
        upload_image = upload.photo_messages(photos=image)[0]
        attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
        if received_message.lower() == "привет":
            write_message(sender, "дарова")
        elif received_message.lower() == "пока":
            write_message(sender, "ну и пошел нахуй")
        else:
            write_message(sender, "да че тебе от меня надо, я не ебу че ты пишешь")
