import requests
from bs4 import BeautifulSoup

COURSE_URL = "https://www.cbr-xml-daily.ru/daily_json.js"
course_req = requests.get(COURSE_URL)
cur = course_req.json()


def get_course():
    cur_usd = cur["Valute"]["USD"]["Value"]
    cur_euro = cur["Valute"]["EUR"]["Value"]
    return f'Курс доллара: {cur_usd}\nКурс евро: {cur_euro}'


KEY_URL = "https://www.cbr.ru/hd_base/KeyRate/"
key_req = requests.get(KEY_URL)
soup = BeautifulSoup(key_req.text, 'lxml')


def get_key():
    data = str(soup.find('body').find('div', {"class": "table"}).find_all('td')[1])[4:]
    key = data[:5]
    return f'Ключевая ставка: {key}%'