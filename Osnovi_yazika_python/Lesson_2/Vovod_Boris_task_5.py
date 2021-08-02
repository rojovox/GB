"""

Группа 1594
Вовод Борис

Задание:
Создать вручную список, содержащий цены на товары (10–20 товаров)

"""

costs = [57.8, 46.51, 97, 25.4, 24.33, 24.5, 29.01, 34, 64, 25, 14.88, 54.23, 12.32]

# Задание A
for i, value in enumerate(costs, 0):
    if len(str(value).split(".")) > 1:df
        if len(str(value).split(".")[1]) > 1:
            print(f'{str(value).split(".")[0]} руб {str(value).split(".")[1]} коп')
        else:
            print(f'{str(value).split(".")[0]} руб 0{str(value).split(".")[1]} коп')
    else:
        print(f'{str(value).split(".")[0]} руб 00 коп')

# Задание B
costs.sort()
print(costs)

# Задание C
costs_descending = costs
costs_descending.reverse()
print(costs_descending)

# Задание D
print(str(costs[4::-1]))