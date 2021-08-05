"""

Группа 1594
Вовод Борис

Задание:
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)

"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В']

tutors_klasses = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))

print(*tutors_klasses, sep='\n')
