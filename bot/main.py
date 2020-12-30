import telebot
import random
from bot.Constants import SVYAT_FRAZES, MALOI_FRAZES, NAMES, TEXT

bot = telebot.TeleBot('1432193307:AAECkUzfBCtsBZnKrAfoxR5AuCH9SQwTK5I')



def read_photo():
    path = r'C:\Users\Win10Pro\Documents\photo'
    rand = random.randrange(1, 44, 1)
    full_path = f'{path}\{rand}.jpg'
    with open(full_path, 'rb') as f:
        return f.read()

@bot.message_handler(content_types=['text'])
def check_who(message):
    print(f'{message.text} это сообщение от {message.from_user.first_name} - {message.from_user.id} ')
    if message.from_user.id == 590521699:
        bot.send_message(message.chat.id, random.choice(SVYAT_FRAZES))
    if message.from_user.id == 240714315:
        bot.send_message(message.chat.id, random.choice(MALOI_FRAZES))

@bot.message_handler(content_types=['text'], regexp='Аркаша')
def get_text_message(message):
    talk_with_me(message)

@bot.message_handler(commands=['help'])
def get_command_help(message):
    bot.send_message(message.chat.id, TEXT)

def talk_with_me(message):
    if "прив" in message.text.lower():
        bot.send_message(message.chat.id, f"Привет, {NAMES[message.from_user.id]}")
    elif 'поздр' in message.text.lower():
        bot.send_message(message.chat.id, f'Поздравляю, {check_whom(message.text)}' )
        bot.send_message(message.chat.id, get_text_cong())
        bot.send_photo(message.chat.id, read_photo())
    else:
        bot.send_message(message.chat.id, "Я ещё глупенький, не все понимаю. Но уже умнее Свята")


def get_text_cong():
    path = r'C:\Users\Win10Pro\congrat'
    rand = random.randrange(1, 14, 1)
    full_path = f'{path}\{rand}.TXT'
    with open(full_path, 'rb') as f:
        return f.read()


def check_whom(msg: str):
    phrase = msg.lower().split()
    if 'свят' in phrase[-1]:
        return 'Свят'
    elif 'анто' in phrase[-1]:
        return 'Антон'
    elif 'ром' in phrase[-1] or 'мол' in phrase[-1]:
        return 'Рома'
    elif 'тан' in phrase[-1]:
        return 'Таня'
    elif 'ник' in phrase[-1]:
        return 'Ник'
    elif 'ан' in phrase[-1]:
        return 'Аня'


bot.polling(none_stop=True, interval=0)