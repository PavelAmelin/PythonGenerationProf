# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет самого старшего сотрудника из данного списка.

from datetime import datetime

patt, d = '%d.%m.%Y', {}
for _ in range(int(input())):
    data = input().split()
    d.setdefault(datetime.strptime(data[2], patt), []).append((data[:2]))
res = sorted(d.items())[0]
if len(res[1]) > 1:
    print(res[0].strftime(patt), len(res[1]))
else:
    print(res[0].strftime(patt), *res[1][0])