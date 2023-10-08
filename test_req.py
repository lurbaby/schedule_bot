import requests

response = requests.get('https://schedule.kpi.ua/?groupId=5ccb849f-57aa-460d-9f0c-545d81e69bfc')


print(response.text)