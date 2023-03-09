from datetime import date
import calendar

def ThirdThursday(year):
    all_thursday = {}
    for mon in range(1, 13):
        for week in calendar.monthcalendar(year, mon):
            thus = week[3]
            if thus:
                all_thursday.setdefault(mon, []).append(date(year, mon, thus).strftime('%d.%m.%Y'))
    return [all_thursday[k][2] for k in all_thursday.keys()]

print(*ThirdThursday(int(input())), sep='\n')