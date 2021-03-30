import telebot

from telebot import types

bot = telebot.TeleBot("1760088503:AAEuAemvSa77HwEJ8pRuxsyzkv8kT47NmTA", parse_mode=None)
name = ''
surname = ''
age = 0
data = []


def send_goodbye(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item_cash = types.KeyboardButton('Да')
    item_card = types.KeyboardButton('Нет')
    markup_reply.add(item_cash, item_card)
    if 'big' in data[0].keys():
        pizza = 'большую'
    else:
        pizza = 'маленькую'
    value = data[0].values()
    text = f"Вы хотите {pizza} пиццу оплата - {' '.join(value)} ?"
    bot.send_message(message.chat.id, text,
                     reply_markup=markup_reply)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_big = types.KeyboardButton('Большую')
    item_small = types.KeyboardButton('Маленькую')
    markup_inline.add(item_big, item_small)
    bot.send_message(message.chat.id, 'Какую вы хотите пиццу? Большую или маленькую?',
                     reply_markup=markup_inline)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text == 'Большую':
        data.append({'big': None})
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_cash = types.KeyboardButton('Наличкой')
        item_card = types.KeyboardButton('Картой')
        markup_reply.add(item_cash, item_card)
        bot.send_message(message.chat.id, 'Выберите способ оплаты',
                         reply_markup=markup_reply)

    elif message.text == 'Маленькую':
        data.append({'small': None})
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_cash = types.KeyboardButton('Наличкой')
        item_card = types.KeyboardButton('Картой')
        markup_reply.add(item_cash, item_card)
        bot.send_message(message.chat.id, 'Выберите способ оплаты',
                         reply_markup=markup_reply)

    if message.text == 'Наличкой' and 'big' in data[0].keys():
        data[0]['big'] = 'наличкой'
        print(data)
        send_goodbye(message)

    elif message.text == 'Картой' and 'big' in data[0].keys():
        data[0]['big'] = 'картой'
        send_goodbye(message)

    elif message.text == 'Наличкой' and 'small' in data[0].keys():
        data[0]['small'] = 'наличкой'
        send_goodbye(message)

    elif message.text == 'Картой' and 'small' in data[0].keys():
        data[0]['small'] = 'картой'
        send_goodbye(message)

    if message.text == 'Да':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Спасибо за заказ курьер едет", reply_markup=markup_reply)
        data.clear()
    elif message.text == 'Нет':
        data.clear()
        markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_big = types.KeyboardButton('Большую')
        item_small = types.KeyboardButton('Маленькую')
        markup_inline.add(item_big, item_small)
        bot.send_message(message.chat.id, 'Какую вы хотите пиццу? Большую или маленькую?',
                         reply_markup=markup_inline)


bot.polling()
