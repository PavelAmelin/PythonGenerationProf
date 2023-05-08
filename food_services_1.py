# Write a program that determines the district of Moscow with
# the largest number of establishments, identifies
# the restaurant chain with the largest number of establishments

import json

with open('food_services.json', 'r', encoding='utf-8') as file:
    lst_rest, distr, chain = json.load(file), {}, {}
    for dct in lst_rest:
        distr[dct['District']] =distr.get(dct['District'], 0) + 1
        if dct['OperatingCompany']:
            chain[dct['OperatingCompany']] = chain.get(dct['OperatingCompany'], 0) + 1
    max_distr = max(distr.keys(), key=lambda k: distr[k])
    max_chain = max(chain.keys(), key=lambda k: chain[k])
    print(f'{max_distr}: {distr[max_distr]}', f'{max_chain}: {chain[max_chain]}', sep='\n')
