# Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
# Напишите программу, которая принимает на вход текущие дату и время и определяет,
# сколько времени осталось до выхода курса.

from datetime import datetime

def choose_plural(amount: int, declensions: tuple) -> str:
    if 21 <= amount % 100 <= 99 or 1 <= amount % 100 <= 9:
        if amount % 10 == 1:
            return f'{amount} {declensions[0]}'
        elif 2 <= amount % 10 <= 4:
            return f'{amount} {declensions[1]}'
    return f'{amount} {declensions[2]}'

patt, d, h, m = '%d.%m.%Y %H:%M', ('день', 'дня', 'дней'), ('час', 'часа', 'часов'), ('минута', 'минуты', 'минут')
delta = datetime(2022, 11, 8, 12) - datetime.strptime(input(), patt)
a, b, c = delta.days, delta.seconds // 3600, delta.seconds // 60 % 60
days, hours, minutes = choose_plural(a, d), choose_plural(b, h), choose_plural(c, m)
if a >= 1 and b > 0:
    print(f'До выхода курса осталось: {days} и {hours}')
elif a >= 1 and b == 0:
    print(f'До выхода курса осталось: {days}')
elif a == 0 and b >= 1 and c > 0:
    print(f'До выхода курса осталось: {hours} и {minutes}')
elif a == 0 and b >= 1 and c == 0:
    print(f'До выхода курса осталось: {hours}')
elif a == 0 and b == 0 and c > 0:
    print(f'До выхода курса осталось: {minutes}')
elif a == 0 and b == 0 and c == 0 or a < 0:
    print('Курс уже вышел!')