# Write a program that adds all the missing keys to each
# JSON object in the given list, setting these keys to null

import json

with open('people.json', 'r', encoding='utf-8') as file:
    lst = json.load(file)
    all_keys = {k for dct in lst for k in dct.keys()}
    for dct in lst:
        for k in all_keys:
            if k not in dct:
                dct[k] = None
      
with open('updated_people.json', 'w', encoding='utf-8') as out:
    json.dump(lst, out, indent=3)
