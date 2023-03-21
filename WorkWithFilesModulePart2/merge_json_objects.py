# Write a program that merges two given JSON objects into one JSON object

import json

with open('data1.json', 'r', encoding='utf-8') as file1, open('data2.json', 'r', encoding='utf-8') as file2:
    lst1, lst2 = json.load(file1), json.load(file2)
    for k in lst2:
        lst1.update({k: lst2[k]})

with open('data_merge.json', 'w', encoding='utf-8') as out:
    json.dump(lst1, out, indent=3)
