"""
 CheckiO platform has a similar mission Verify Anagrams, but in it you have to determine whether words are anagrams.
 In this mission, the task will be a little different. You are given two strings and need to determine whether you
 can swap two letters in the first string to get the second string. If so (or words are the same) -
 return True, if not - False.

For example, the string "btry", if we swap y and t, we get "byrt".

Input: Two strings (str).

Output: Logic value (bool).
"""


def switch_strings(line: str, result: str) -> bool:
    if line == result:
        return True
    elif len(line) != len(result):
        return False

    first, second = [], []
    for x, y in zip(line, result):
        if x != y:
            first.append(x)
            second.append(y)
    if len(first) != 2:
        return False

    return True if set(first) == set(second) else False


print("Example:")
print(switch_strings("btry", "byrt"))

# These "asserts" are used for self-checking
assert switch_strings("btry", "byrt") == True
assert switch_strings("boss", "boss") == True
assert switch_strings("solid", "disel") == False
assert switch_strings("false", "flaes") == False
assert switch_strings("true", "treu") == True