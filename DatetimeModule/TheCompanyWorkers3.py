# Дан список сотрудников организации, в котором указаны их
# фамилии, имена и даты рождения. Напишите программу,
# которая определяет самого молодого сотрудника, празднующего
# свой день рождения в течение ближайших семи дней от текущей даты.

from datetime import datetime, timedelta

patt, data, res = '%d.%m.%Y', [], []
today = int(datetime.strptime(input(), patt).strftime('%j'))
for _ in range(int(input())):
    *name, birthday = input().split()
    bd = datetime.strptime(birthday, patt)
    data.append((' '.join(name), bd, int(bd.strftime('%j'))))
for dt in data:
    a = (dt[2] - today) % 365
    if a <= 7 and a != 0:
        res.append((dt[0], dt[1]))
print(max(res, key=lambda x: x[1])[0] if len(res) > 0 else 'Дни рождения не планируются')