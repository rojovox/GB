"""

Группа 1594
Вовод Борис

Задание:
Создать список, состоящий из кубов нечётных чисел от 1 до 1000:

"""

cube_list = []
# Создание списка чисел
for i in range(1, 1000, 2):
    cube_list.append(i**3)

# Задание a
sum_list = 0
for i in range(0, len(cube_list)):
    # Начало расчёта суммы цифр i-го элемента списка
    hand_parser_sum = 0
    hand_parser_body = cube_list[i]
    while hand_parser_body != 0:
        hand_parser_sum += hand_parser_body % 10
        hand_parser_body = hand_parser_body // 10
        # Конец расчёта суммы цифр i-го элемента списка
    if hand_parser_sum % 7 == 0:
        sum_list += cube_list[i]
print(sum_list)

# Задание b+с
sum_list = 0
for i in range(0, len(cube_list)):
    # Начало расчёта суммы цифр i-го элемента списка
    hand_parser_sum = 0
    cube_list[i] = cube_list[i] + 17  # Добавление числа 17 к текущему
    hand_parser_body = cube_list[i]
    while hand_parser_body != 0:
        hand_parser_sum += hand_parser_body % 10
        hand_parser_body = hand_parser_body // 10
        # Конец расчёта суммы цифр i-го элемента списка
    if hand_parser_sum % 7 == 0:
        sum_list += cube_list[i]
print(sum_list)