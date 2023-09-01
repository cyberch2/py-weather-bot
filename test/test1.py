import telebot
from telebot import types

bot = telebot.TeleBot('6296801723:AAFpHYA2rM8e6c7HUgEclejlYwjWI_fKhZQ')


def keyboard():
    your_text = ""
    answer = ""
    keyboard1 = types.InlineKeyboardMarkup()
    key_n1 = types.InlineKeyboardButton(text=your_text, callback_data=answer)
    keyboard1.add(key_n1)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/reg":
        keyboard.your_text = "Конечно!"
        keyboard.answer = "Yes"
        question = "Начнем?)"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard())
        bot.register_next_step_handler(message, city)
    else:
        bot.send_message(message.from_user.id, "Напиши /reg")


def city(message):
    pass


bot.polling(none_stop=True, interval=0)
