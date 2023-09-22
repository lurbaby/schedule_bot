import telebot
from telebot import types
from get_text import *

bot = telebot.TeleBot('6500439714:AAH738daeLTRG8uAdyoepcwEOh7qRh7T_KU')
print('start')


@bot.message_handler(commands=['start'])
def start_msg(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='📚Розклад занять')
    # btn2 = types.KeyboardButton(text='Викладачі')
    kb.add(btn1)

    bg_png = open('bg_2.png', 'rb')
    bot.send_photo(message.chat.id, bg_png, caption='<b>Вітаю тебе в помічнику РТФ!</b> \n\n👨🏻‍🎓Тут ви можете швидко подивитися розклад своєї групи!\n\n🔅Напишіть назву вашої групи через дефіс наприклад РЕ-31',
                   parse_mode='HTML', reply_markup=kb)
    bg_png.close()



@bot.message_handler(func=lambda m: True)
def wrong_msg(message, mode=1):

    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]

    def auth():
        if message.text == days[0]:
            bot.send_message(message.chat.id, f"<b>Розклад на Понеділок : </b>"
                                              f"\n\n1. Вступ до спеціальності\n\t(Адаменко В.О.)"
                                              f"\n\n2. Вступ до спеціальності\n\t(Адаменко В.О.)"
                                              f"\n\n3. Інформатика. Частина 1\n\t(Товкач І.О. ,Катін П.Ю.)",
                             parse_mode='HTML')
        if message.text == days[1]:
            bot.send_message(message.chat.id, f"<b>Розклад на Вівторок : </b>"
                                              f"\n\n1. Аналітична геометрія та лінійна алгебра\n\t(Павленков В.В.)"
                                              f"\n\n2. Інженерна та комп’ютерна графіка. Частина 1\n\t(Гнітецька Г.О.)"
                                              f"\n\n3. Загальна фізика. Частина 1\n\t(Репалов І.М.)", parse_mode='HTML')
        if message.text == days[2]:
            bot.send_message(message.chat.id, f"<b>Розклад на Середу : </b>"
                                              f"\n\n1. Здоровий сон запорука успіху\n\t(Ясо сухуй 2000 років до н.е.)"
                                              f"\n\n2. Математичний аналіз. Частина 1\n\t(Маслюк Г.О.)"
                                              f"\n\n3. Основи здорового способу життя\n\t(Мартинов Ю.О.)"
                                              f"\n\n4. Інженерна та комп’ютерна графіка. Частина 1\n\t(Гнітецька Г.О.)",
                             parse_mode='HTML')
        if message.text == days[3]:
            bot.send_message(message.chat.id, f"<b>Розклад на Четвер : </b>"
                                              f"\n\n1. Інформатика. Частина 1\n\t(Вишневий С.В.)"
                                              f"\n\n2. Математичний аналіз. Частина 1\n\t(Диховичний О.О.)"
                                              f"\n\n3. Основи здорового способу життя (2-10)\n\t(Саламаха О.Є.)",
                             parse_mode='HTML')
        if message.text == days[4]:
            bot.send_message(message.chat.id, f"<b>Розклад на П'ятницю</b>"
                                              f"\n\n1. Здоровий сон запорука успіху\n\t(Ясо Cухуй 2000 років до н.е.)"
                                              f"\n\n2. Практичний курс іноземної мови. Частина 1\n\t(Чіжова Н.В.)"
                                              f"\n\n3. Загальна фізика. Частина 1\n\t(Репалов І.М.)"
                                              f"\n\n4. Аналітична геометрія та лінійна алгебра\n\t(Маслюк Г.О.)"
                                              f"\n\n5. Інформатика. Частина 1. Основи програмування та алгоритми\n\t(Товкач І.О.,Катін П.Ю.)",
                             parse_mode='HTML')

    if mode == 1:

        if (message.text != days[0] and
            message.text != days[1] and
            message.text != days[2] and
            message.text != days[3] and
            message.text != days[4])and (message.text != "📚Розклад занять") and (message.text).lower() != "ре-31":
            bot.send_message(message.chat.id,
                             "<b>🚫Схоже ви ввели невірну команду🚫</b>\n\n <b>Cкористайтеся командами в меню!👇</b>",
                             parse_mode='HTML')
        else:

            kb_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text=days[0])
            btn2 = types.KeyboardButton(text=days[1])
            btn3 = types.KeyboardButton(text=days[2])
            btn4 = types.KeyboardButton(text=days[3])
            btn5 = types.KeyboardButton(text=days[4])
            btn6 = types.KeyboardButton(text="")
            kb_2.add(btn1, btn2, btn3, btn4, btn5)

            if (message.text).lower() == "ре-31":
                bot.send_message(message.chat.id, '<b>Виберіть потрібний день в меню внизу!👇!</b>', reply_markup=kb_2, parse_mode='HTML')
        auth()


#перевірка на медіа файли
@bot.message_handler(content_types=['photo', 'video', 'document', 'animation', 'sticker'])
def media_error(message):
    bot.send_message(message.chat.id, "<b>😡Не потрібно засмічувати цей чат😡</b>", parse_mode='HTML')




bot.infinity_polling()