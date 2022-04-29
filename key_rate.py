import requests
from bs4 import BeautifulSoup

URL = "https://www.cbr.ru/hd_base/KeyRate/"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'lxml')


def get_key():
    data = str(soup.find('body').find('div', {"class": "table"}).find_all('td')[1])[4:]
    key = data[:5]
    return f'Ключевая ставка: {key}%'
