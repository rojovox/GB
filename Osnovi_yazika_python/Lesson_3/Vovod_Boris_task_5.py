"""

Группа 1594
Вовод Борис

Задание:
Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

"""

from random import randrange

def get_jokes(count):
    result = []
    i = 0
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    while i < count:
        result.append((nouns[randrange(len(nouns))]) + ' ' +
                      (adverbs[randrange(len(adverbs))]) + ' ' +
                      (adverbs[randrange(len(adjectives))]))
        i += 1
    return result

print(get_jokes(5))


