"""
 Determine whether a sequence of elements is ascending such that each of its elements is strictly larger than (and not merely equal to) the preceding element. Empty sequence is considered as ascending.

example

Input: List with integers (int).

Output: Logic value (bool).
"""
from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    # items = [4, 5, 6, 7, 3, 7, 9]
    items2 = items.copy()
    items2.sort()
    return (items == items2 and len(set(items)) > 1) or not items or len(items) == 1


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False