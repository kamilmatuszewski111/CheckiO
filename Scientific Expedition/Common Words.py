"""
 Let's continue examining words. You are given two strings with words separated by commas. Try to find what is common between these strings. The words in the same string don't repeat.

Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings (str).

Output: The common words as a string (str).


How it is used: Here you can learn how to work with strings and sets. This knowledge can be useful for linguistic analysis.

Preconditions:

    Each string contains no more than 10 words;
    All words are separated by commas;
    All words consist of lowercase latin letters.

"""


def checkio(line1: str, line2: str) -> str:
    a = []
    for i in line1.split(','):
        if i in list(line2.split(',')):
            a.append(i)
    return ','.join(sorted(a))


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'