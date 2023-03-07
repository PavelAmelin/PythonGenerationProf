# Функция is_available_date() должна возвращать True, если дата или период date_for_booking
# полностью доступна для бронирования. В противном случае функция должна возвращать False.

from datetime import date

def GetSet(st: str) -> set:
    s = set()
    if '-' in st:
        start = [int(i) for i in st.split('-')[0].split('.')]
        end = [int(i) for i in st.split('-')[1].split('.')]
        c = date(start[2], start[1], start[0]).toordinal()
        d = date(end[2], end[1], end[0]).toordinal()
        for i in range(c, d + 1):
            s.add(i)
    else:
        one = [int(i) for i in st.split('.')]
        s.add(date(one[2], one[1], one[0]).toordinal())
    return s

def is_available_date(lst_dates: list, str_dates: str) -> bool:
    all_reserve = set()
    for dt in lst_dates:
        all_reserve |= GetSet(dt)
    return len(all_reserve & GetSet(str_dates)) == 0


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))