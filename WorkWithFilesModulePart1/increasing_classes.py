# Write a program that writes the given table to the
# sorted_student_counts.csv file, arranging all columns
# in ascending order of classes, if classes match, in ascending letter order

import csv

with open('student_counts.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.DictReader(file))
    classes = [i.split('-') for i in rows[0]][1:]
    classes.sort(key=lambda x: (int(x[0]), x[1]))
    year_clas = ['year'] + ['-'.join(i) for i in classes]

with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as out:
    wr = csv.DictWriter(out, fieldnames=year_clas)
    wr.writeheader()
    wr.writerows(rows)
