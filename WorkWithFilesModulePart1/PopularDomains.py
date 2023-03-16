# Write a program that creates a file domain_usage.csv,
# where the first column contains the name of the mail domain,
# and the second column contains the number of users using this domain

import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    rows, d = list(csv.reader(file))[1:], {}
    for row in rows:
        name, domain = ' '.join(row[:2]), row[2].split('@')[1]
        d[domain] = d.get(domain, []) + [name]
    res = sorted([[k, len(d[k])] for k in d.keys()], key=lambda x: (x[1], x[0]))
with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['domain', 'count'])
    w.writerows(res)
