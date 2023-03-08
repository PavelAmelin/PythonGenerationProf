# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year

import calendar
from datetime import date

def get_days_in_month(year, month):
    m = list(calendar.month_name).index(month)
    AllMonth = [date(year, m, i) for i in range(1, calendar.monthrange(year, m)[1] + 1)]
    return AllMonth

print(get_days_in_month(2021, 'December'))

