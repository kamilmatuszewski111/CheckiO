"""
 You have a text and a sequence of words. You need to check if the words in sequence appear in the same order as in the given text.

example

Cases you should expect while solving this challenge:

    a word from the sequence is not in the text - your function should return False;
    any word can appear more than once in a text - use only the first one;
    two words in the given sequence are the same - your function should return False;
    the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
    the text includes only English letters and spaces.

Input: Two arguments. The first one is a given text as a string (str), the second is list of words as strings (str).

Output: Logic value (bool).
"""

def words_order(text: str, words: list) -> bool:
    kupa = []
    for i in words:
        if i not in text.split(" "):
            return False
        kupa.append(text.split(" ").index(i)) if i in text.split(" ") else None
    kupa2 = kupa.copy()
    kupa2.sort()
    kupa2 = set(kupa2)
    return True if list(kupa2) == kupa else False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False