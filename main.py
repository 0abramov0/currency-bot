from config import *
from get_rate import *
from key_rate import *
from keyboards import *


@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Hi!', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def rate(message):
    if message.text == 'Курс' + '\N{money bag}':
        bot.send_message(message.chat.id, get_course())
        bot.send_message(message.chat.id, get_key())


bot.infinity_polling(timeout=10, long_polling_timeout=5)
