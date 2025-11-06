"""Question-9. Leap Year Checker
"""


def check_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


year = int(input("Enter the year: "))

leap_year = check_leap_year(year)

if leap_year:
    print(f"Hy there, {year} year is a leap year!")
else:
    print(f"Hy there, {year} year is a not leap year!")
