# Write a program that creates a JSON object whose key is the administrative
# district and the value is a JSON object, in which the key is the name of
# the district that belongs to this administrative district, and the value
# is a list of addresses of all playgrounds in this district

import json
import csv

with open('playgrounds.csv', 'r', encoding='utf-8') as file:
    all_parks, res = csv.DictReader(file, delimiter=';'), {}
    for dct in all_parks:
        res.setdefault(dct['AdmArea'], {}).setdefault(dct['District'], []).append(dct['Address'])

with open('addresses.json', 'w', encoding='utf-8') as out:
    json.dump(res, out, indent=3, ensure_ascii=False)
