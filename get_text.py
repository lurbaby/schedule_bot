from bs4 import BeautifulSoup
import requests
url = 'http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=fa1a9406-067e-4e0e-9c37-f726ca1f9a06'
def get_html(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")
    main_table = soup.find_all("table")

    return main_table

def sort_all_elements(main, n_table=0):
    skip_index = 0
    days = [[], [], [], [], [], []]
    extacted_elements = [[], [], [], [], [], []]


    index = 0
    flag = False

    for items in main:
        if n_table == 0:
            n_table += 1
            continue

        parsed_table = items.find_all('td')
        for element in parsed_table:
            if skip_index == 0 or skip_index == 7:
                skip_index = 1
                continue

            if flag:
                index = 0
                flag = False
            if index == 5:
                flag = True

            days[index].append(element)

            index += 1
            skip_index += 1

        if n_table == 1:
            break

    def print_elements():

        for day in range(len(days)):
            for element_second in range(len(days[day])):
                temp = days[day][element_second].find_all('a')
                for values in temp:
                    # if len(str(values.text)) == 0:
                    #     print('-')
                    #     continue
                    # print(type(values.text))

                    if str(values.text)[0].isdigit():

                        print(str(values.text)[7:])
                        continue
                    print(values.text)
                print('\n')
            print('\n\n')

    print_elements()
    print()
    return days



week_1 = sort_all_elements(get_html(url), 1)
week_2 = sort_all_elements(get_html(url), 0)

def extract_info(week):

    extacted_elements = [[], [], [], [], [], []]


    for day in range(len(week)):
        for element_second in range(len(week[day])):
            extacted_elements[day].append(week[day][element_second].find('span'))
            # for last_element in range(len(week[day][element_second])): [last_element]

    return extacted_elements

# test = extract_info(week_1)

# print('\n\n\n\n')
# for i in range(len(week_1)):
#     for j in range(len(week_1[i])):
#         print(week_1[i][j])
# print('\n\n\n\n')
#
# for i in range(len(week_2)):
#     for j in range(len(week_2[i])):
#         print(week_2[i][j])

# for i in range(len(test)):
#
#     for j in range(len(test[i])):
#         print(f"{j} Element : ", test[i][j])
#
#
# print('\n\n\n\n')



# for i in range(len(week_1)):
#     for j in range(len(week_1[i])):
#         print(f"{j} Element : ", week_1[i][j])
# print('\n\n\n\n')


