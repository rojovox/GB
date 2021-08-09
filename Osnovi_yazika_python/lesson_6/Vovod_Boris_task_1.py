"""

Группа 1594
Вовод Борис

Задание:
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

"""

file = open("nginx_logs.txt", "r", encoding="utf-8")

with file:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in file)
    for i in content:
        print(i)
