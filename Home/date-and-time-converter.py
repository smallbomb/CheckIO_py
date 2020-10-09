# https://py.checkio.org/en/mission/date-and-time-converter/

'''
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.
'''

from datetime import datetime

"""
Day 1
'%d'  --> '01'
'%-d' --> '1'  not on windows
'%#d' --> '1'  only on windows
'%_d' --> ' 1' not on windows, and it has leading spaces instead.
From what I tested, it works for a lot of "%?":
Years, months, hours (12 or 24-hour clock), weeks, days, minutes, seconds...
"""

def date_time(time: str) -> str:
    date = datetime.strptime(time, '%d.%m.%Y %H:%M')
    h = "s" * (date.hour != 1)
    m = "s" * (date.minute != 1)
    return date.strftime(f"%-d %B %Y year %-H hour{h} %-M minute{m}")


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
