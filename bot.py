import telebot
from telebot import types
from config import TOKEN
from my_weather import get_weather

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Погода', callback_data='weather')
    btn2 = types.InlineKeyboardButton('Книги', callback_data='books')
    btn3 = types.InlineKeyboardButton('Фильмы', callback_data='cinema')
    btn4 = types.InlineKeyboardButton('ТОП Шазам', callback_data='music')
    btn5 = types.InlineKeyboardButton('Поиск информации', callback_data='search')
    btn6 = types.InlineKeyboardButton('Новости', callback_data='news')
    btn7 = types.InlineKeyboardButton('Выйти', callback_data='exit')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    text = "Привет, я твой бот. Выбирай дальнейшие действия."
    bot.send_message(message.chat.id, text, reply_markup=markup)

def send_weather_info(message):
    city = message.text
    text = get_weather(city)
    bot.send_message(message.chat.id,  text)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'weather':

                bot.send_message(call.message.chat.id, "Напишите название города")
                bot.register_next_step_handler(call.message, send_weather_info)
            elif call.data == 'exit':
                bot.send_message(call.message.chat.id, reply_markup=markup)

            else:
                print('bi')

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
