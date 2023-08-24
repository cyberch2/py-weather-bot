import telebot;
from telebot import types
bot = telebot.TeleBot('6296801723:AAFpHYA2rM8e6c7HUgEclejlYwjWI_fKhZQ')
name = ""
surname = ""
age = 0

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, "Напиши /reg")

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Напишите вашу фамилию")
    bot.register_next_step_handler(message,get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько вам лет")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Цифрами, пожалуйста");
            return

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Да", callback_data ='Yes')
        keyboard .add(key_yes)
        key_no = types.InlineKeyboardButton(text="Нет", callback_data='No')
        keyboard.add(key_no)
        question = 'Тебе ' +str(age), ' лет, тебя зовут' +name+' '+surname+'?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
        break



@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    global age
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
        return(get_age)


bot.polling(none_stop=True, interval=0)



