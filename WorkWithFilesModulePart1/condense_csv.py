# The function should convert the contents of the file into the usual CSV format
# by grouping the rows by the first column and naming the first column id_name

import csv

def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as file:
        rows, d, res = list(csv.reader(file)), {}, []
        positions = sorted(set(row[0] for row in rows))
        for i in positions:
            d[id_name] = d.get(id_name, []) + [i]
        for row in rows:
            d[row[1]] = d.get(row[1], []) + [row[2]]
        for i in range(len(positions)):
            res.append([val[i] for val in d.values()])
    with open('condensed.csv', 'w', encoding='utf-8') as f:
        writ = csv.writer(f)
        writ.writerow(list(d.keys()))
        writ.writerows(res)

print(condense_csv('data_2.csv', id_name='Position'))
