print("This is a file from GitHub repository")

print('These are new local changes')

import requests

api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)    # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:     # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)     # При другом коде ответа выводим этот код


api_url = 'http://numbersapi.com/43'

response = requests.get(api_url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)