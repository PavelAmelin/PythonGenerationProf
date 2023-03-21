# Write a program that determines the appropriate pool

import json

with open('pools.json', 'r', encoding='utf-8') as file:
    lst_pools, res = json.load(file), []
    for pool in lst_pools:
        wrk_mon = pool['WorkingHoursSummer']['Понедельник']
        start, end = int(wrk_mon.split('-')[0][:2]), int(wrk_mon.split('-')[1][:2])
        if start <= 10 and end >= 12:
            res.append((pool['Address'], pool['WorkingHoursSummer'], pool['DimensionsSummer']))
    result = sorted(res, key=lambda x: (-x[2]['Length'], -x[2]['Width']))[0]
    print(f"{result[2]['Length']}x{result[2]['Width']}", result[0], sep='\n')
