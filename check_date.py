from datetime import datetime


def check_date():
    today = datetime.now()

    date = today.strftime('%A')

    return date == "Monday"


a = 1
if check_date():

    with open('day_db.txt', 'r') as read_date:
        if str(read_date.read()) == '1':
            a = 0
            with open('day_db.txt', 'w') as change_date:
                change_date.write('0')
    print(a)
else:
    print(a)
