# Даны две даты — левая и правая границы диапазона соответственно.
# Напишите программу, которая из этого диапазона, включая границы, выводит, начиная с даты,
# у которой сумма дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг.

from datetime import datetime, timedelta

pat = '%d.%m.%Y'
start, end = datetime.strptime(input(), pat), datetime.strptime(input(), pat)

while (start.day + start.month) % 2 == 0:
    start += timedelta(1)
while start <= end:
    if start.isoweekday() != 1 and start.isoweekday() != 4:
        print(start.strftime(pat))
    start += timedelta(3)