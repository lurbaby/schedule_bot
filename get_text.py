from bs4 import BeautifulSoup
import requests

url2 = 'http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=0698046f-fdc3-4ef8-bf4b-c720989e9ae5'
response = requests.get(url2)
# print(response)

soup = BeautifulSoup(response.text, "lxml")

main = soup.find_all("table")
# print(main)
count = 0
for items in main:
    if count == 0:
        count += 1
        continue

    # print(items.find_all('td'))
    parsed_table = items.find_all('td')
    for element in parsed_table:
        print(element)

    count += 1
