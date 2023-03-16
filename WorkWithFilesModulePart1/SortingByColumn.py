# Write a program that sorts the contents of a given file by a given column

import csv

column = int(input()) - 1
with open('deniro.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file))
    for row in sorted(rows, key=lambda x: int(x[column]) if x[column].isdigit() else x[column]):
        print(*row, sep=',')
