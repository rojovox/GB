"""

Группа 1594
Вовод Борис

Задание:
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.

Комментарий:
Запуск из файла ulils.py

"""

from requests import get, utils


def currency_rates(currency):
    url_data = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))
    content = url_data.split("Valute ID=")
    for i in content:
        if currency.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))
