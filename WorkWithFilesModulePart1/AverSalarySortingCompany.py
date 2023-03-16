# Write a program that sorts companies in ascending order of the average salary
# of their employees and prints their names, each on a separate line.

import csv

with open('salary_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    salaries = {}
    for row in list(rows)[1:]:
        salaries.setdefault(row[0], []).append(int(row[1]))
print(*sorted(salaries.keys(), key=lambda k: sum(salaries[k]) / len(salaries[k])), sep='\n')
