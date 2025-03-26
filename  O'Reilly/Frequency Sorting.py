"""
 Sort the given sequence so that its elements should be grouped and those groups end up in the decreasing frequency order, that is, the number of times element appears in the sequence. If two elements have the same frequency, their groups should end up according to the natural order of elements. For example:

example

If you want to practice more with the similar case, try Sort Array by Element Frequency mission.

Input: List of integers (int).

Output: List or another Iterable (tuple, iterator, generator) of integers (int).



"""
from typing import List


def frequency_sorting(numbers: List[int]) -> List[int]:
    freq = {number: numbers.count(number) for number in set(numbers)}
    return sorted(numbers, key=lambda x: (-freq[x], x))


if __name__ == "__main__":
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [
        4,
        4,
        4,
        3,
        3,
        11,
        11,
        7,
        13,
    ], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [
        10,
        10,
        21,
        21,
        55,
        55,
        99,
        99,
    ], "Reversed"