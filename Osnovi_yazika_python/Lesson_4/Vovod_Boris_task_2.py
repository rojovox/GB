"""

Группа 1594
Вовод Борис

Задание:
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.

"""
from requests import get, utils

url_data = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(currency):
    content = url_data.split("Valute ID=")
    for i in content:
        if currency.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(currency_rates(input()))
