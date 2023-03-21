 # Write a program that creates a single JSON object that
# has as a key the name of a religion and as a value a
# list of countries where that religion is practiced

import json

with open('countries.json', 'r', encoding='utf-8') as file:
    lst_countr, relig_countr = json.load(file), {}
    for dct in lst_countr:
        relig_countr.setdefault(dct['religion'], []).append(dct['country'])

with open('religion.json', 'w', encoding='utf-8') as out:
    json.dump(relig_countr, out, indent=3)