import telebot
from telebot import types

bot = telebot.TeleBot('6574600871:AAE152BFZ9nk7gQwhrU2Uk8Z1VdfTnuw4Qc')

@bot.message_handler(commands=['Кнопочки'])
def group_bot(message):

    buttons = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Скинути ДЗ","Показати всі ДЗ"]
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text=buttons[0])
    btn2 = types.KeyboardButton(text=buttons[1])
    btn3 = types.KeyboardButton(text=buttons[2])
    btn4 = types.KeyboardButton(text=buttons[3])
    btn5 = types.KeyboardButton(text=buttons[4])
    btn6 = types.KeyboardButton(text=buttons[5])
    btn7 = types.KeyboardButton(text=buttons[6])
    # btn6, btn7
    kb.add(btn1, btn2, btn3, btn4, btn5)

    bot.reply_to(message, "Висилаю команди нижче👇", reply_markup=kb)

@bot.message_handler(content_types=['text'])
def send_response(message):
    buttons = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Скинути ДЗ", "Показати всі ДЗ"]
    if message.text == buttons[0]:
        bot.send_message(message.chat.id, f"<b>Розклад на Понеділок : </b>"
                                          f"\n\n1. Вступ до спеціальності\n\t(Адаменко В.О.)"
                                          f"\n\n2. Вступ до спеціальності\n\t(Адаменко В.О.)"
                                          f"\n\n3. Інформатика. Частина 1\n\t(Товкач І.О. ,Катін П.Ю.)",
                         parse_mode='HTML')
    if message.text == buttons[1]:
        bot.send_message(message.chat.id, f"<b>Розклад на Вівторок : </b>"
                                          f"\n\n1. Аналітична геометрія та лінійна алгебра\n\t(Павленков В.В.)"
                                          f"\n\n2. Інженерна та комп’ютерна графіка. Частина 1\n\t(Гнітецька Г.О.)"
                                          f"\n\n3. Загальна фізика. Частина 1\n\t(Репалов І.М.)", parse_mode='HTML')
    if message.text == buttons[2]:
        bot.send_message(message.chat.id, f"<b>Розклад на Середу : </b>"
                                          f"\n\n1. Здоровий сон запорука успіху\n\t(Ясо сухуй 2000 років до н.е.)"
                                          f"\n\n2. Математичний аналіз. Частина 1\n\t(Маслюк Г.О.)"
                                          f"\n\n3. Основи здорового способу життя\n\t(Мартинов Ю.О.)"
                                          f"\n\n4. Інженерна та комп’ютерна графіка. Частина 1\n\t(Гнітецька Г.О.)",
                         parse_mode='HTML')
    if message.text == buttons[3]:
        bot.send_message(message.chat.id, f"<b>Розклад на Четвер : </b>"
                                          f"\n\n1. Інформатика. Частина 1\n\t(Вишневий С.В.)"
                                          f"\n\n2. Математичний аналіз. Частина 1\n\t(Диховичний О.О.)"
                                          f"\n\n3. Основи здорового способу життя (2-10)\n\t(Саламаха О.Є.)",
                         parse_mode='HTML')
    if message.text == buttons[4]:
        bot.send_message(message.chat.id, f"<b>Розклад на П'ятницю</b>"
                                          f"\n\n1. Здоровий сон запорука успіху\n\t(Ясо Cухуй 2000 років до н.е.)"
                                          f"\n\n2. Практичний курс іноземної мови. Частина 1\n\t(Чіжова Н.В.)\nhttps://us04web.zoom.us/j/74088613872?pwd=UCgJKQhE7lbhME9GbrPp5EXWgxwldZ.1"
                                          f"\n\n3. Загальна фізика. Частина 1\n\t(Репалов І.М.)\nhttps://meet.google.com/xzh-bwfv-ozw"
                                          f"\n\n4. Аналітична геометрія та лінійна алгебра\n\t(Маслюк Г.О.)\nhttps://us05web.zoom.us/j/85040954927?pwd=ka9oyjEQmDL8bLh5Nk0dIbI4aaUkbU.1"
                                          f"\n\n5. Інформатика. Частина 1. Основи програмування та алгоритми\n\t(Товкач І.О.,Катін П.Ю.)\nhttps://us04web.zoom.us/j/76929094074?pwd=Lwawar6m275VtmbVcK6aOqil0PbA16.1",
                         parse_mode='HTML')

bot.infinity_polling()