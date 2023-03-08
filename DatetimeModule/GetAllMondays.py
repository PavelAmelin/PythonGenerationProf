from datetime import date, timedelta

def get_all_mondays(year):
    begin, end, delta = date(year, 1, 1), date(year, 12, 31), timedelta(7)
    first_monday = begin + timedelta((7 - begin.weekday()) % 7)
    res = []
    while first_monday <= end:
        res.append(first_monday)
        first_monday += delta
    return res

print(get_all_mondays(1353))
