from telebot import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = 'Курс' + '\N{money bag}'
keyboard.add(button1)
