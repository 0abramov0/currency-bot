import requests

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
r = requests.get(URL)
cur = r.json()


def get_course():
    cur_usd = cur["Valute"]["USD"]["Value"]
    cur_euro = cur["Valute"]["EUR"]["Value"]
    return f'Курс доллара: {cur_usd}\nКурс евро: {cur_euro}'
