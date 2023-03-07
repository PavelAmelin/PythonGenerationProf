# Напишите программу, которая принимает на вход текущие дату и время и
# определяет количество минут, оставшееся до закрытия магазина.

from datetime import datetime, timedelta

work_hours = {1: '9:00 - 21:00', 2: '9:00 - 21:00', 3: '9:00 - 21:00', 4: '9:00 - 21:00', 5: '9:00 - 21:00',
              6: '10:00 - 18:00', 7: '10:00 - 18:00'}
pat = '%d.%m.%Y %H:%M'
now = datetime.strptime(input(), pat)
op_cl = work_hours[now.isoweekday()].split(' - ')
open = datetime.strptime(now.strftime('%d.%m.%Y') + ' ' + op_cl[0], pat)
close = datetime.strptime(now.strftime('%d.%m.%Y') + ' ' + op_cl[1], pat)
print(('Магазин не работает', (close - now).seconds // 60)[open <= now < close])
