# Write a program that writes the given table to the
# sorted_student_counts.csv file, arranging all columns
# in ascending order of classes, if classes match, in ascending letter order

import csv

with open('student_counts.csv', 'r', encoding='utf-8') as file:
    rows, result = csv.DictReader(file), []
    for row in rows:
        year = list(row.items())[0]
        classes = list((cl.split('-'), cnt) for cl, cnt in row.items())[1:]
        sort_classes = sorted(classes, key=lambda x: (int(x[0][0]), x[0][1]))
        d = {'-'.join(cl[0]): cl[1] for cl in sort_classes}
        result.append({**{year[0]: year[1]}, **d})

with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as out:
    wr = csv.DictWriter(out, fieldnames=list(result[0].keys()))
    wr.writeheader()
    wr.writerows(result)
