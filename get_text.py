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
    index = 0
    flag = False

    for items in main:
        if n_table == 0:
            n_table += 1
            continue

        # print(items.find_all('td'))
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

            if (len(element.text) == 0):
                days[index].append("-")

            days[index].append(element.text)

            # print(days[index])
            index += 1
            skip_index += 1

        if n_table == 1:
            break

    return days


week_1 = sort_all_elements(get_html(url), 1)
week_2 = sort_all_elements(get_html(url), 0)


# print('\n\n\n\n')
for i in range(len(week_1)):
    for j in range(len(week_1[i])):
        print(week_1[i][j])
print('\n\n\n\n')

for i in range(len(week_2)):
    for j in range(len(week_2[i])):
        print(week_2[i][j])
