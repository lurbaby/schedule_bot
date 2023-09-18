from selenium import webdriver

# class="sc-gFqAkR deYOvn"

driver = webdriver.Firefox()


url = 'http://roz.kpi.ua/'  # Замініть це на URL вашої сторінки
url2 = 'http://epi.kpi.ua/Schedules/ViewSchedule.aspx?g=0698046f-fdc3-4ef8-bf4b-c720989e9ae5'
driver.get(url2)

# element = driver.find_elements('sc-gFqAkR deYOvn')

html_code = driver.page_source

# Зберегти HTML-код у файл
with open('output2.html', 'w', encoding='utf-8') as file:
    file.write(html_code)

# Закрити браузер
driver.quit()