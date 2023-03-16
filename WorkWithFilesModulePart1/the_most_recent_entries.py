# Write a program that selects only the most recent entries for
# each user from the file name_log.csv and writes them to the
# file new_name_log.csv

import csv
from datetime import datetime

patt = '%d/%m/%Y %H:%M'
with open('name_log.csv', 'r', encoding='utf-8') as file:
    rows, d, res = list(csv.reader(file))[1:], {}, []
    for name, email, dtime in rows:
        d.setdefault(email, []).append((datetime.strptime(dtime, patt), name))
    for email in d:
        res.append((max(d[email])[1], email, datetime.strftime(max(d[email])[0], patt)))
    res = sorted(res, key=lambda x: x[1])
with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as f:
    writ = csv.writer(f)
    writ.writerow(['username', 'email', 'dtime'])
    writ.writerows(res)
