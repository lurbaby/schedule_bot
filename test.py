import pandas as pd



tables = pd.read_html('http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=fa1a9406-067e-4e0e-9c37-f726ca1f9a06')

# len(tables)
tb = tables[0]

days = ['1 08:30', '2 10:25', '3 12:20', '4 14:15', '5 16:10', '6 18:30']
index = 0
index_2 = 0

# Пройдіться по всім стовпцям таблиці і виведіть значення вертикально
for column in tb.columns:
    # print(f"Стовпець {column}:")
    if index == 0:
        index += 1
        continue

    for value in tb[column]:
        if index_2 == 5:
            index_2 = 0

        print(value)
        index_2 += 1
    print()  # Додати порожній рядок між стовпцями
    index += 1
