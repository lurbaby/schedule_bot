import telebot
from telebot import types

bot = telebot.TeleBot('6500439714:AAH738daeLTRG8uAdyoepcwEOh7qRh7T_KU')
print('start')


@bot.message_handler(commands=['start'])
def start_msg(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Розклад занять')
    btn2 = types.KeyboardButton(text='Викладачі')
    kb.add(btn1, btn2, )

    bg_png = open('bg.png', 'rb')
    bot.send_photo(message.chat.id, bg_png, caption='<b>Вітаю тебе в помічнику РТФ!</b> \n\n👨🏻‍🎓 Доступні наступні функції:\n- розклад студентів\nсповіщення за 5 хв\n',
                   parse_mode='HTML', reply_markup=kb)
    bg_png.close()
bot.polling()