"""
 You are given a positive number. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

example

Input: A positive integer (int).

Output: The product of the digits as an integer (int).
"""


def checkio(number: int) -> int:
    liczba = 1
    a = [int(x) for x in str(number) if int(x)]
    for i in a:
        liczba *= i
    return liczba


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1