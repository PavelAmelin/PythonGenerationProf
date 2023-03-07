# Дана последовательность дат. Напишите программу, которая создает и выводит список,
# элементами которого являются неотрицательные целые числа — количество дней между
# двумя соседними датами последовательности.

from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
dts = [datetime.strptime(dt, pattern) for dt in input().split()]
print([abs(dts[i + 1] - dts[i]).days for i in range(len(dts) - 1)])