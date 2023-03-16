# The function must return a dictionary
# where the key is the name of the filename column
# and the value is a list of the elements of this column

import csv

def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file))
        res, header, dat = {}, rows[0], rows[1:]
        for ind, k in enumerate(header):
            for j in range(len(dat)):
                res.setdefault(k, []).append(dat[j][ind])
        return res

print(csv_columns('exam.csv'))

