"""
 You are given the lengths for each side on a triangle. You need to find all three angles for this triangle. If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles as 0 (zero). The angles should be represented as a list of integers in ascending order . Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).

triangle-angles

Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.
"""


from typing import List
from math import acos, degrees, ceil, floor


def checkio(a: int, b: int, c: int) -> List[int]:
    if a+b <= c or a+c <= b or b+c <= a:
        return [0, 0, 0]

    A = lambda a, b, c: degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    B = lambda a, b, c: degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    C = lambda a, b, c: degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    math_round = lambda x: ceil(x) if x - int(x) >= 0.5 else floor(x)

    return sorted([math_round(A(a, b, c)), math_round(B(a, b, c)), math_round(C(a, b, c))])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"