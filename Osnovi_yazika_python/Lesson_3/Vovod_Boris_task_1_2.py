"""

Группа 1594
Вовод Борис

Задание:
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися
с заглавной буквы — результат тоже должен быть с заглавной.

Комментарий:
Реализовано сразу задание №2

"""

diction = {'zero': 'Ноль', 'one': 'Один', 'two': 'Два', 'three': 'Три', 'four': 'Четыре', 'five': 'Пять',
           'six': 'Шесть', 'seven': 'Семь', 'eight': 'Восемь', 'nine': 'Девять'}


def number_converter(temp):
    if temp[0].isupper():
        return diction.get(temp.lower())
    else:
        return diction.get(temp.lower()).lower()


print(number_converter(input()))
