import requests
# импорт реквестов для гет и не только запросов
from .read_json import read_json
# тут подключаем функцию для преобразования джсона в объект пайтон
import json
# ну это вообще модуль джон, круто!
data_api = read_json(name_file= 'config_api.json')
# считываем конфиг файл
API_KEY = data_api['api_key']
# по ключу api_key берем ключ и пишем в переменную
CITY_NAME = data_api['city_name']
# так же с названием города
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# f строка для гет запроса на сервак погоды по ключу апи
response = requests.get(URL)
# собственно сам гет запрос, пишем ответ в переменную
if response.status_code == 200:
    # если нас не послали подальше
    data_dict = json.loads(response.content)
    # получаем джсон с ответа
    print(json.dumps(data_dict, indent= 4))
