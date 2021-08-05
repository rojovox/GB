"""

Группа 1594
Вовод Борис

Задание:
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

"""


import sys


def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


for i in odd_nums(int(input())):
    print(i)

