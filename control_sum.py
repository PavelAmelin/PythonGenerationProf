# Write a program that calculates a checksum for an object
# contained in a pickle file and compares it to a given integer

import pickle

filename = input()
contr_sum = int(input())

with open(filename, 'rb') as f:
    obj = pickle.load(f)
    if type(obj) is dict:
        contr_sum_obj = sum(el for el in obj.keys() if type(el) is int)
    elif type(obj) is list:
        res_lst = [el for el in obj if type(el) is int]
        if len(res_lst) == 0:
            contr_sum_obj = 0
        else:
            contr_sum_obj = max(res_lst) * min(res_lst)
print(('Контрольные суммы не совпадают', 'Контрольные суммы совпадают')[contr_sum == contr_sum_obj])