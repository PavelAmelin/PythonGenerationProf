# Write a program that determines whether a given
# sequence is a progression, and if so, determines its form.

from sys import stdin

lst = [int(i.strip()) for i in stdin]
if all(lst[i + 2] - lst[i + 1] == lst[i + 1] - lst[i] for i in range(len(lst) - 2)):
    print('Арифметическая прогрессия')
elif all(lst[i + 2] / lst[i + 1] == lst[i + 1] / lst[i] for i in range(len(lst) - 2)):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
