# Функция должна возвращать количество суббот между датами start и end включительно.

from datetime import date

def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    a = [date.fromordinal(i).weekday() for i in range(start.toordinal(), end.toordinal() + 1)]
    return a.count(5)

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))