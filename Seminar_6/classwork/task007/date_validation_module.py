# Задание №7
# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию.

_YEAR_BOUNDS = (1, 9999)
_MONTH_DAYS = {
    1: 31,
    2: (28, 29),
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def _is_leap_year(year: int):
    return not year % 4 and year % 100 or not year % 400


def is_possible_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))

    if _YEAR_BOUNDS[0] < year < _YEAR_BOUNDS[1]:
        if month in _MONTH_DAYS:
            if month == 2 and _is_leap_year(year):
                max_days = _MONTH_DAYS[month][1]
            elif month == 2:
                max_days = _MONTH_DAYS[month][0]
            else:
                max_days = _MONTH_DAYS[month]

            if day in range(1, max_days + 1):
                return True

    return False


print(is_possible_date('03.11.2023'))
print(is_possible_date('29.02.2023'))
print(is_possible_date('29.02.2000'))
