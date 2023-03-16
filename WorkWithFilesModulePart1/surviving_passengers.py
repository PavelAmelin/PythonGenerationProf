# Write a program that prints out the names of
# surviving passengers who were less than 18 years

import csv

with open('titanic.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))[1:]
    survivors = list(filter(lambda x: int(x[0]) == 1 and float(x[3]) < 18, rows))
    for i in sorted(survivors, key=lambda x: x[2], reverse=True):
        print(i[1])