import telebot
from telebot import types

bot = telebot.TeleBot('6296801723:AAFpHYA2rM8e6c7HUgEclejlYwjWI_fKhZQ')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_n1 = types.KeyboardButton("Конечно!")
    keyboard1.add(key_n1)
    question = ('Привет, это WeatherBot. Бот, который показывает погоду в нужном тебе городе! Чтобы начать работу, '
                'нажми кнопку "Конечно". Начнем?)')
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard1)
    bot.register_next_step_handler(message, city)


@bot.message_handler(content_types=['text'])
def city(message):
    if message.text == "Конечно!":
        bot.send_message(message.from_user.id, "Давай разберемся с тобой в каком городе ты живешь) Напиши свой город)")
    else:
        bot.send_message(message.from_user.id, "Нажми на кнопку))))")


bot.polling(none_stop=True, interval=0)
