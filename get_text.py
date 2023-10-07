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

    for day in range(len(days)):
        for element_second in range(len(days[day])):
            current_element = days[day][element_second].find_all('a')

            #skip day name
            if (element_second == 0):
                continue

            if (len(current_element) != 0):
                for find_text in range(len(current_element)):

                    extacted_elements[day].append(current_element[find_text].text)
                    # print(current_element[find_text].text, end=' ')
                # print()
            else:
                # print(current_element)
                extacted_elements[day].append(current_element)
            # print(len(current_element))

        # print()
    return extacted_elements


def replace_wrong_sort_by_lessons(extacted_elements):
    final_array = [
                   [ [], [], [], [], [], [] ],
                   [ [], [], [], [], [], [] ],
                   [ [], [], [], [], [], [] ],
                   [ [], [], [], [], [], [] ],
                   [ [], [], [], [], [], [] ],
                   [ [], [], [], [], [], [] ]
                  ]

    for every_day in range(len(extacted_elements)):
        lesson_index = 0

        for lessons in range(len(extacted_elements[every_day])):

            if len(extacted_elements[every_day][lessons]) == 0:
                if lessons != 0:
                    lesson_index += 1
                final_array[every_day][lesson_index].append('-')
                continue

            if extacted_elements[every_day][lessons][0].isupper() and lessons != 0:
                lesson_index += 1

            final_array[every_day][lesson_index].append(extacted_elements[every_day][lessons])

    for day_element in final_array:
        for subject_element in day_element:

            skip_cabinet_index = 0

            for each_element_of_subject in subject_element:

                if each_element_of_subject[0].isdigit():
                    skip_cabinet_index += 1
                    continue


    return final_array


week_1 = replace_wrong_sort_by_lessons(sort_all_elements(get_html(url), 1))
week_2 = sort_all_elements(get_html(url), 0)

for i in week_1:
    for j in i:
        print(j)
    print()