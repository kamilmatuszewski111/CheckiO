"""
Check if the given year is leap year. A year is a leap year if it is divisible by 4,
except for end-of-century years which must be divisible by 400. This means that the year 2000 was a leap year,
although 1900 was not.
"""


def is_leap_year(year: int) -> bool:
    if not year % 100:
        return False if year % 400 else True
    else:
        return False if year % 4 else True


print("Example:")
print(is_leap_year(1891))

# These "asserts" are used for self-checking
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2020) == True
assert is_leap_year(2021) == False
assert is_leap_year(1600) == True
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(2400) == True