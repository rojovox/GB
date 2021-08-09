"""

Группа 1594
Вовод Борис

Задание:
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём
данных в файлах во много раз меньше объема ОЗУ.

"""

from json import dump
from itertools import zip_longest

with open("hobby.csv", "r", encoding="utf-8") as hobby:
    with open("users.csv", "r", encoding="utf-8") as users:
        users_hobby = zip_longest((" ".join(user.split(",")) for user in users), hobby, fillvalue=None)
        uh_dict = {str(el[0]).strip(): (str(el[1]).strip()) if el[0] else exit(1) for el in users_hobby}

        file = open("dict.json", "w", encoding="utf-8")
        with file:
            dump(uh_dict, file, ensure_ascii=False, indent=4)
            print(uh_dict)
