"""

Группа 1594
Вовод Борис

Задание:
Дан список. Необходимо его обработать

Комменатрий:
Задание 2 и 3

"""


def number_converter(temp):
    for i1, value1 in enumerate(temp, 0):
        # Дополнение однозначного числа до двухзначного путем добавления нуля и 1 стадия добавления кавычек
        if temp[i1][0].isdigit():
            if len(temp[i1]) < 2:
                temp[i1] = '0' + temp[i1][0]
            temp.insert(i1 + 1, '"')
        # Дополнение однозначного числа до двухзначного путем добавления нуля
        # при условии, что перед числом стоит плюс, либо минус и 1 стадия добавления кавычек
        if temp[i1][0] == '+' or temp[i1][0] == '-':
            if len(temp[i1]) == 2:
                temp[i1] = temp[i1][0] + '0' + temp[i1][1]
            temp.insert(i1 + 1, '"')
    temp.reverse()
    return temp


temperature = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

temperature = number_converter(temperature)
temperature = number_converter(temperature)

# if .isdigit()
flag = bool(0)
# print(type(flag))
for i, value in enumerate(temperature, 0):
    if value == '"':
        if flag == 0:
            flag = 1
        else:
            flag = 0
    print(value, end='')
    if flag == 0:
        print(' ', end='')
