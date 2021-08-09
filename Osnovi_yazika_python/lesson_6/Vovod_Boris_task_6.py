"""

Группа 1594
Вовод Борис

Задание:
Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной
строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение
суммы продаж.

"""

from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as donut_a:
    with open("bakery.csv", "r", encoding="utf-8") as donut_r:
        if len(argv) == 1:
            print(donut_r.read())
        elif len(argv) == 2:
            if "," in argv[1] or "." in argv[1]:
                print(f'{round(float(argv[1].replace(",", ".")), 3)}', file=donut_a)
            else:
                print(*(v for i, v in enumerate(donut_r) if i >= int(argv[1]) - 1))
        elif len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(donut_r) if start - 1 <= i < finish), sep="")
