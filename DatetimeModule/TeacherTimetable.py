# Репетитор по математике проводит занятия по 45 минут с перерывами по
# 10 минут. Репетитор обозначает время начала рабочего дня и время окончания
# рабочего дня. Напишите программу, которая генерирует и выводит расписание занятий.

from datetime import datetime, timedelta

start, end = input(), input()
pat = '%H:%M'
t_st, t_en = datetime.strptime(start, pat), datetime.strptime(end, pat)
lesson, brk = timedelta(minutes=45), timedelta(minutes=10)
while t_st <= t_en - lesson:
    print(f'{t_st.strftime(pat)} - {(t_st + lesson).strftime(pat)}')
    t_st += lesson + brk