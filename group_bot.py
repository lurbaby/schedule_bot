import telebot
from telebot import types

bot = telebot.TeleBot('6574600871:AAE152BFZ9nk7gQwhrU2Uk8Z1VdfTnuw4Qc')

@bot.message_handler(commands=['Бот'])
def group_bot(message):

    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця","Скинути ДЗ","Показати всі ДЗ"]
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text=days[0])
    btn2 = types.KeyboardButton(text=days[1])
    btn3 = types.KeyboardButton(text=days[2])
    btn4 = types.KeyboardButton(text=days[3])
    btn5 = types.KeyboardButton(text=days[4])
    btn6 = types.KeyboardButton(text="")
    kb.add(btn1, btn2, btn3, btn4, btn5)

    bot.reply_to(message, "Висилаю команди нижче👇", reply_markup=kb)




bot.infinity_polling()