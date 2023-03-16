# Write a program that determines and displays the
# cheapest product and the name of the store where it is sold

import csv

with open('prices.csv', 'r', encoding='utf-8') as file:
    rows, all_prod = csv.DictReader(file, delimiter=';'), {}
    for row in rows:
        all_prod.setdefault(row['Магазин'], []).extend([(k, v) for k, v in list(row.items())[1:]])
    min_price_shop = [(k, *min(all_prod[k], key=lambda x: int(x[1]))) for k in all_prod]
    cheapest = min(min_price_shop, key=lambda x: (int(x[2]), x[1]))
    print(f'{cheapest[1]}: {cheapest[0]}')