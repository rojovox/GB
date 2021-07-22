"""

Группа 1594
Вовод Борис

Задание:
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности

"""

# CONST
SEC_IN_MIN = 60
SEC_IN_HOUR = 3600
SEC_IN_DAY = 86400

duration = int(input())  # Получим входное значение
output_time = []

# Считаем дни
days_in_duration = duration // SEC_IN_DAY
if days_in_duration > 0:
    output_time.append(str(days_in_duration) + ' days')
# Считаем часы
hours_in_duration = (duration - (SEC_IN_DAY * days_in_duration)) // SEC_IN_HOUR
if hours_in_duration > 0:
    output_time.append(str(hours_in_duration) + ' hours')
# Считаем минуты
min_in_duration = (duration - (days_in_duration * SEC_IN_DAY) - (hours_in_duration * SEC_IN_HOUR)) // SEC_IN_MIN
if min_in_duration > 0:
    output_time.append(str(min_in_duration) + ' min')
# Считаем секунды
sec_in_duration = duration % SEC_IN_MIN
if sec_in_duration > 0:
    output_time.append(str(sec_in_duration) + ' sec')

print(f'duration = {duration}')
print(' '.join(output_time))
