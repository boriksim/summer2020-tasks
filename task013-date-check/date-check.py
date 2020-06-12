# 2020-06-12
# Проверка даты
# Написать функцию, которая проверяет правильность указанной даты в формате YYYY-MM-DD.
import re


def check_date(date):
    date_re = re.match(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", date)
    if date_re is None:
        return False
    year = int(date_re.group(1))
    month = int(date_re.group(2))
    day = int(date_re.group(3))
    if year > 0 and 0 < month <= 12 and 0 < day <= 31:
        if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
            if (month == 2 and (day > 29 or day < 0)) or (
                    month <= 7 and month % 2 != 0 and day == 31) or (
                    month >= 8 and month % 2 == 0 and day == 31):
                return False
            else:
                return True
        else:
            if (month == 2 and (day > 28 or day < 0)) or (
                    month <= 7 and month % 2 == 0 and day == 31) or (
                    month >= 8 and month % 2 != 0 and day == 31):
                return False
            else:
                return True
    else:
        return False


dates = [
    "2020-10-10",
    "2020-20-10",
    "2020-02-30",
    "2020-01-32",
    "2020-02-29",
    "2021-02-29",
    "202102-29",
    "20210229",
    "",
    "ВАСЯ",
    "Василий Иванович Крузинштейн",
]
for d in dates:
    print(d, ": ", check_date(d))
