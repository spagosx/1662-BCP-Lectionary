import datetime

lookup_table = {
    0: (3, 27),
    1: (4, 14),
    2: (4, 3),
    3: (3, 23),
    4: (4, 11),
    5: (3, 31),
    6: (4, 18),
    7: (4, 8),
    8: (3, 28),
    9: (4, 16),
    10: (4, 5),
    11: (3, 25),
    12: (4, 13),
    13: (4, 2),
    14: (3, 22),
    15: (4, 10),
    16: (3, 30),
    17: (4, 17),
    18: (4, 7),
    19: (3, 27)
}

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def find_easter(year):
    # find calculation for look up table
    # get full moon
    # find Sunday after full moon

    calculus = ((year - (int(year / 19) * 19)) + 1)
    moon = lookup_table[calculus]
    moon_date = datetime.date(year=year, month=moon[0], day=moon[1])
    easter = next_weekday(moon_date, 6)
    print(easter)
    return easter


input_year = input()
find_easter(int(input_year))
