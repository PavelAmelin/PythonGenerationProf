# Write a program that creates a list whose elements are
# the objects from the list contained in the data.json file

import json

with open('data.json', 'r', encoding='utf-8') as file:
    lst_obj, result = json.load(file), []
    for obj in lst_obj:
        if type(obj) is str:
            result.append(obj + '!')
        elif type(obj) is int:
            result.append(obj + 1)
        elif type(obj) is bool:
            result.append(not obj)
        elif type(obj) is list:
            result.append(obj * 2)
        elif type(obj) is dict:
            obj['newkey'] = None
            result.append(obj)
        elif type(obj) is None:
            continue

with open('updated_data.json', 'w', encoding='utf-8') as out:
    json.dump(result, out, indent=3)


