# write a program that determines order of the dates in a given sequence

from sys import stdin
from datetime import datetime

dates = [datetime.strptime(d.strip(), '%d.%m.%Y') for d in stdin]
more, less = [], []
for i in range(len(dates) - 1):
    more.append((dates[i + 1] - dates[i]).days > 0)
    less.append((dates[i + 1] - dates[i]).days < 0)
if all(less):
    print('DESC')
elif all(more):
    print('ASC')
else:
    print('MIX')

