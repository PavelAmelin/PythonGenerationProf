# Write a program that determines all types of establishments
# and for each type finds the largest establishment of this
# type (has the largest number of seats)

import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    lst_rest, rest_types = json.load(file), {}
    for dct in lst_rest:
        rest_types.setdefault(dct['TypeObject'], []).append((dct['Name'], dct['SeatsCount']))
    for k, v in sorted(rest_types.items()):
        max_seats = max(v, key=lambda x: x[1])
        print(f'{k}: {max_seats[0]}, {max_seats[1]}')


