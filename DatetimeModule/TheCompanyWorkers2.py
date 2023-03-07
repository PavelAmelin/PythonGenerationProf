# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет,
# в какую из дат родилось больше всего сотрудников.

from datetime import datetime, timedelta

patt, dt, res = '%d.%m.%Y', {}, []
for _ in range(int(input())):
    data = input().split()
    dt[datetime.strptime(data[2], patt)] = dt.get(datetime.strptime(data[2], patt), 0) + 1

for k, val in sorted(dt.items()):
    if val == max(dt.values()):
        print(k.strftime(patt))