# Write a program that identifies students who match the following conditions:
# age 18 years old or more course progress 75 % or more
import csv
import json

with open('students.json', 'r', encoding='utf-8') as file:
    lst_students, res = json.load(file), []
    for info in lst_students:
        if info['age'] >= 18 and info['progress'] >= 75:
            res.append((info['name'], info['phone']))
    res.sort()

with open('data.csv', 'w', encoding='utf-8', newline='') as out:
    wr = csv.writer(out)
    wr.writerow(['name', 'phone'])
    wr.writerows(res)
