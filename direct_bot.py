import telebot
from telebot import types, custom_filters
from get_text import *
from check_date import check_date
from telebot.types import ReplyKeyboardRemove

# states
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage




bot = telebot.TeleBot('6500439714:AAH738daeLTRG8uAdyoepcwEOh7qRh7T_KU', parse_mode='HTML')
print('start')
days = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота"]

class current_states(StatesGroup):

    group_name = State()
    select_day = State()

groups = {
              'ре-31':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=fa1a9406-067e-4e0e-9c37-f726ca1f9a06",
              'рі-31':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=23cfdbc6-1e36-4f3d-b1bf-3645e1a73361",
              'рі-32':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=a3e7025c-b393-49a8-b914-0654f23541bc",
              'рс-31':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=0698046f-fdc3-4ef8-bf4b-c720989e9ae5",
              'рі-п31':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=123f25c6-82d0-4c70-9931-fec1a2bfe3c0",
              'ре-31мп':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=f22013e7-11e8-45a1-91dc-d20a5384b315",
              'рс-31мп': "http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=2acfc079-2a61-4c25-b193-b06973e4fb3d",
              'ре-21мн': "http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=fe02a87f-2965-4864-8ada-6e090a8e368c",
              'рі-21мн':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=a30fc710-3ada-4188-ba3a-4339b515c02b",
              'рс-21мн':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=a30fc710-3ada-4188-ba3a-4339b515c02b",
              'ре-21мп':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=894a483c-7817-422f-8407-85012cdbb552",
              'рі-21мп':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=c32b8825-a5bf-4541-9b2a-bf1198c8ea51",
              'рс-21мп':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=5e2d9504-5570-4751-a029-1ceebf592fd2",




              'ре-21':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=b037d505-6e78-4900-8691-7651009b2ce9",
              'ре-22':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=6241332b-f071-47dc-86a4-a685a51f7e3c",
              'рі-21':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=88249ead-8697-4b80-b0d9-7bac6ff748a9",
              'рс-21':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=c8220e00-039e-43aa-bd85-b58593b9973c",
              'рі-п21':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=fd34ccca-0440-4b1f-9cc9-6c1e7fefa0a0",
              'рс-п21':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=5c9b3de2-376c-492b-a3f8-4bbcdfec0b69",
              'ре-11':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=aac4d740-23ed-46ef-b4c4-c57baf20cdee",
              'ре-12':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=c3ec9ab2-6a9e-4ac9-a54a-8f3434016bdd",
              'рі-11':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=c974ae19-2cd8-4cd5-8ee9-5efb9428b11a",
              'рс-11':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=b0aa1a46-a9a8-4977-ad12-4091c4b9ebe4",
              'ре-п11':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=6a114965-aa6f-4d27-931d-91506eb4bd7d",
              'рі-п11':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=e7ac8fed-8ab3-4eb2-8dc0-d995725ef075",
              'рс-п11':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=954c7183-7bca-49bd-ab57-462c1cf3c0a1",
              'ре-01':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=97d51a67-6638-4585-801c-2b85d2786919",
              'ре-02':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=b4dc21b1-64e0-4387-8e4f-6345956cc2e5",
              'рі-01':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=2ba936ac-812b-4d25-bc95-277bead4c308",
              'рс-01':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=8530f1db-2236-40fd-96e7-c15a9d3f7a0e",
              'ре-31мн':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=e9f0d998-bb95-4a2f-9532-92a5f4b87185",
              'рі-31мн':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=cba20702-d1b8-4314-b33c-4d29f3dc7269",
              'рс-31мн':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=44ec3095-bc91-49ba-90de-8cc1c196ad19",
              'рі-31мп':"http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=05eb79d2-5480-401f-bdd7-8ef8a7162660",

              }


def auth(message, week):
    final_msg = ""
    numbers_list = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
    emoji_list = ['🎓', '📍', '🕒']
    show_time = ['8:30 - 9:55', '10:25 - 12:00', '12:20 - 13:55', '14:15 - 15:50', '16:10 - 18:10']
    show_time_index = 0
    emoji_index = 0

    len_4_flag = False

    for msg in range(len(week)):

        if msg == 0 and message.text == days[0]:

            final_msg += '<b>Розклад на Понеділок : </b>\n➖➖➖➖➖➖➖➖➖➖\n'

            for subject in range(len(week[msg])):

                if subject > 4:
                    continue

                if emoji_index <= 4:
                    final_msg += numbers_list[emoji_index]
                    emoji_index += 1

                if len(week[msg][subject]) == 1:
                    final_msg += f"❌\n{emoji_list[0]}❌\n{emoji_list[1]}❌\n"
                else:
                    if len(week[msg][subject]) == 4:
                        week[msg][subject][1] += ' ' + week[msg][subject][2]
                        week[msg][subject].pop(2)
                        len_4_flag = True

                    for subject_elements in range(len(week[msg][subject])):

                        test = week[msg][subject][subject_elements]

                        if subject_elements == 0:
                            final_msg += '<b>' + week[msg][subject][subject_elements] + '</b>' + '\n'

                        elif subject_elements == 1:
                            final_msg += emoji_list[0] + week[msg][subject][subject_elements] + '\n'

                        elif subject_elements == 2:
                            final_msg += emoji_list[1] + week[msg][subject][subject_elements] + '\n'

                if show_time_index <= 4:
                    final_msg += f' {emoji_list[2]}{show_time[show_time_index]}\n➖➖➖➖➖➖➖➖➖➖\n'
                    show_time_index += 1

            bot.send_message(message.chat.id, f"{final_msg}", parse_mode='HTML')

        elif msg == 1 and message.text == days[1]:

            final_msg += '<b>Розклад на Вівторок : </b>\n➖➖➖➖➖➖➖➖➖➖\n'

            for subject in range(len(week[msg])):

                if subject > 4:
                    continue

                if emoji_index <= 4:
                    final_msg += numbers_list[emoji_index]
                    emoji_index += 1

                if len(week[msg][subject]) == 1:
                    final_msg += f"❌\n{emoji_list[0]}❌\n{emoji_list[1]}❌\n"
                else:
                    if len(week[msg][subject]) == 4:
                        week[msg][subject][1] += ' ' + week[msg][subject][2]
                        week[msg][subject].pop(2)
                        len_4_flag = True

                    for subject_elements in range(len(week[msg][subject])):

                        test = week[msg][subject][subject_elements]

                        if subject_elements == 0:
                            final_msg += '<b>' + week[msg][subject][subject_elements] + '</b>' + '\n'

                        elif subject_elements == 1:
                            final_msg += emoji_list[0] + week[msg][subject][subject_elements] + '\n'

                        elif subject_elements == 2:
                            final_msg += emoji_list[1] + week[msg][subject][subject_elements] + '\n'

                if show_time_index <= 4:
                    final_msg += f' {emoji_list[2]}{show_time[show_time_index]}\n➖➖➖➖➖➖➖➖➖➖\n'
                    show_time_index += 1

            bot.send_message(message.chat.id, f"{final_msg}", parse_mode='HTML')

        elif msg == 2 and message.text == days[2]:

            final_msg += '<b>Розклад на Середу : </b>\n➖➖➖➖➖➖➖➖➖➖\n'

            for subject in range(len(week[msg])):

                if subject > 4:
                    continue

                if emoji_index <= 4:
                    final_msg += numbers_list[emoji_index]
                    emoji_index += 1

                if len(week[msg][subject]) == 1:
                    final_msg += f"❌\n{emoji_list[0]}❌\n{emoji_list[1]}❌\n"
                else:
                    if len(week[msg][subject]) == 4:
                        week[msg][subject][1] += ' ' + week[msg][subject][2]
                        week[msg][subject].pop(2)
                        len_4_flag = True

                    for subject_elements in range(len(week[msg][subject])):

                        test = week[msg][subject][subject_elements]

                        if subject_elements == 0:
                            final_msg += '<b>' + week[msg][subject][subject_elements] + '</b>' + '\n'

                        elif subject_elements == 1:
                            final_msg += emoji_list[0] + week[msg][subject][subject_elements] + '\n'

                        elif subject_elements == 2:
                            final_msg += emoji_list[1] + week[msg][subject][subject_elements] + '\n'

                if show_time_index <= 4:
                    final_msg += f' {emoji_list[2]}{show_time[show_time_index]}\n➖➖➖➖➖➖➖➖➖➖\n'
                    show_time_index += 1

            bot.send_message(message.chat.id, f"{final_msg}", parse_mode='HTML')

        elif msg == 3 and message.text == days[3]:

            final_msg += '<b>Розклад на Четвер : </b>\n➖➖➖➖➖➖➖➖➖➖\n'

            for subject in range(len(week[msg])):

                if subject > 4:
                    continue

                if emoji_index <= 4:
                    final_msg += numbers_list[emoji_index]
                    emoji_index += 1

                if len(week[msg][subject]) == 1:
                    final_msg += f"❌\n{emoji_list[0]}❌\n{emoji_list[1]}❌\n"
                else:
                    if len(week[msg][subject]) == 4:
                        week[msg][subject][1] += ' ' + week[msg][subject][2]
                        week[msg][subject].pop(2)
                        len_4_flag = True

                    for subject_elements in range(len(week[msg][subject])):

                        test = week[msg][subject][subject_elements]

                        if subject_elements == 0:
                            final_msg += '<b>' + week[msg][subject][subject_elements] + '</b>' + '\n'

                        elif subject_elements == 1:
                            final_msg += emoji_list[0] + week[msg][subject][subject_elements] + '\n'

                        elif subject_elements == 2:
                            final_msg += emoji_list[1] + week[msg][subject][subject_elements] + '\n'

                if show_time_index <= 4:
                    final_msg += f' {emoji_list[2]}{show_time[show_time_index]}\n➖➖➖➖➖➖➖➖➖➖\n'
                    show_time_index += 1

            bot.send_message(message.chat.id, f"{final_msg}", parse_mode='HTML')

        elif msg == 4 and message.text == days[4]:

            final_msg += '<b>Розклад на П\'ятницю : </b>\n➖➖➖➖➖➖➖➖➖➖\n'

            for subject in range(len(week[msg])):

                if subject > 4:
                    continue

                if emoji_index <= 4:
                    final_msg += numbers_list[emoji_index]
                    emoji_index += 1

                if len(week[msg][subject]) == 1:
                    final_msg += f"❌\n{emoji_list[0]}❌\n{emoji_list[1]}❌\n"
                else:
                    if len(week[msg][subject]) == 4:
                        week[msg][subject][1] += ' ' + week[msg][subject][2]
                        week[msg][subject].pop(2)
                        len_4_flag = True

                    for subject_elements in range(len(week[msg][subject])):

                        test = week[msg][subject][subject_elements]

                        if subject_elements == 0:
                            final_msg += '<b>' + week[msg][subject][subject_elements] + '</b>' + '\n'

                        elif subject_elements == 1:
                            final_msg += emoji_list[0] + week[msg][subject][subject_elements] + '\n'

                        elif subject_elements == 2:
                            final_msg += emoji_list[1] + week[msg][subject][subject_elements] + '\n'

                if show_time_index <= 4:
                    final_msg += f' {emoji_list[2]}{show_time[show_time_index]}\n➖➖➖➖➖➖➖➖➖➖\n'
                    show_time_index += 1

            bot.send_message(message.chat.id, f"{final_msg}", parse_mode='HTML')

        elif msg == 5 and message.text == days[5]:

            final_msg += '<b>Розклад на Суботу : </b>\n➖➖➖➖➖➖➖➖➖➖\n'

            for subject in range(len(week[msg])):

                if subject > 4:
                    continue

                if emoji_index <= 4:
                    final_msg += numbers_list[emoji_index]
                    emoji_index += 1

                if len(week[msg][subject]) == 1:
                    final_msg += f"❌\n{emoji_list[0]}❌\n{emoji_list[1]}❌\n"
                else:
                    if len(week[msg][subject]) == 4:
                        week[msg][subject][1] += ' ' + week[msg][subject][2]
                        week[msg][subject].pop(2)
                        len_4_flag = True

                    for subject_elements in range(len(week[msg][subject])):

                        test = week[msg][subject][subject_elements]

                        if subject_elements == 0:
                            final_msg += '<b>' + week[msg][subject][subject_elements] + '</b>' + '\n'

                        elif subject_elements == 1:
                            final_msg += emoji_list[0] + week[msg][subject][subject_elements] + '\n'

                        elif subject_elements == 2:
                            final_msg += emoji_list[1] + week[msg][subject][subject_elements] + '\n'

                if show_time_index <= 4:
                    final_msg += f' {emoji_list[2]}{show_time[show_time_index]}\n➖➖➖➖➖➖➖➖➖➖\n'
                    show_time_index += 1

            bot.send_message(message.chat.id, f"{final_msg}", parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start_msg(message):

    bot.set_state(message.from_user.id, current_states.group_name, message.chat.id)
    with open('bg_2.png', 'rb') as bg_png:
        bot.send_photo(message.chat.id, bg_png, caption='<b>Вітаю тебе в помічнику РТФ!</b> \n\n👨🏻‍🎓Тут ви можете швидко подивитися розклад своєї групи!\n\n🔅Напишіть назву вашої групи через дефіс наприклад ре-31👇')

@bot.message_handler(state=current_states.group_name)
def select_group(message):
    group_name = message.text.lower()

    kb_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text=days[0])
    btn2 = types.KeyboardButton(text=days[1])
    btn3 = types.KeyboardButton(text=days[2])
    btn4 = types.KeyboardButton(text=days[3])
    btn5 = types.KeyboardButton(text=days[4])
    btn6 = types.KeyboardButton(text=days[5])
    btn7 = types.KeyboardButton(text="Вибрати групу ще раз")
    kb_2.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)




    if group_name in groups:
        bot.send_message(message.chat.id, "<b>Ви успішно обрали групу!</b>")
        bot.send_message(message.chat.id, '<b>Виберіть потрібний день в меню внизу!👇</b>', reply_markup=kb_2)
        bot.set_state(message.from_user.id, current_states.select_day)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as state_info:
            state_info['group_name'] = group_name
    else:
        bot.send_message(message.chat.id, "невірне ім'я групи!")



@bot.message_handler(state=current_states.select_day)
def select_day(message):
    day = message.text.lower()

    if day in days:

        with bot.retrieve_data(message.from_user.id, message.chat.id) as state_info:

            schedule_msg = replace_wrong_sort_by_lessons(sort_all_elements(get_html(groups[state_info['group_name']]), 1))

            auth(message, schedule_msg)
    elif day == 'Вибрати групу ще раз'.lower():
        bot.set_state(message.from_user.id, current_states.group_name)
        bot.send_message(message.chat.id, "<b>Напишіть назву вашої групи через дефіс наприклад ре-31</b>",reply_markup=ReplyKeyboardRemove())

    else:
        bot.send_message(message.chat.id, f"Tакого дня немає")


#перевірка на медіа файли
@bot.message_handler(content_types=['photo', 'video', 'document', 'animation', 'sticker'])
def media_error(message):
    bot.send_message(message.chat.id, "<b>😡Не потрібно засмічувати цей чат😡</b>")

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.infinity_polling()


