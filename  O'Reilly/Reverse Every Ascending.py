"""
 Create and return a new Iterable that contains the same elements as the given list items,
 but with the reversed order of the elements inside every maximal strictly ascending subsequence.
 This function should not modify the contents of the original list.

Input: List of integers (int).

Output: List or another Iterable (tuple, iterator, generator) of integers (int).

"""
from typing import Iterable
from typing import List


def reverse_ascending(items: Iterable[int]) -> Iterable[int]:
    temp, final = [], []
    if items:
        for i in range(1, len(items)):
            temp.append(items[i - 1])
            if items[i - 1] >= items[i]:
                final.extend(temp[::-1])
                temp.clear()
        temp.append(items[::-1][0])
        final.extend(temp[::-1])
    return final




print("Example:")
print(list(reverse_ascending([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]