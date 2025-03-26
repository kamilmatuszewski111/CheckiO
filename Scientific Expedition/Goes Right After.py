"""
 In a given word you need to check if one symbol goes only right after another.

Cases you should expect while solving this challenge:

    one of the symbols is not in the given word - your function should return False;
    any symbol appears in a word more than once - use only the first one;
    two symbols are the same - your function should return False;
    the condition is case sensitive, which means 'a' and 'A' are two different symbols.


Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first,
and the third is a symbol (str) that should go after the first one.

Output: A logic value (bool).
"""


def goes_after(word: str, first: str, second: str) -> bool:
    return True if second in word and first in word and word.index(second) - word.index(first) == 1 else False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    assert goes_after("almaz", "r", "l") == False