# Write a program that determines the number of access
# points in each district of Moscow and displays the names
# of all districts, indicating the corresponding number of access points for each

import csv

with open('wifi.csv', 'r', encoding='utf-8') as file:
    rows, d = csv.DictReader(file, delimiter=';'), {}
    for row in rows:
        d[row['district']] = d.get(row['district'], 0) + int(row['number_of_access_points'])
    for k in sorted(d.keys(), key=lambda x: (-d[x], x)):
        print(f'{k}: {d[k]}')