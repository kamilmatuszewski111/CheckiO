"""
 Assuming you are developing a user based system like facebook, you will want to provide the functionality to search for other members regardless of the presence of accents in a username. Without using a 3rd party collation library, you will need to remove the accents from the username before the comparison.

é - letter with an accent; e - letter without an accent; ̀ and ́ - the stand alone accents;


Input: A phrase as a string (unicode).

Output: An accent free Unicode string.
"""


def checkio(in_string):
    import unicodedata

    return ''.join(c for c in unicodedata.normalize('NFD', in_string)
                   if unicodedata.category(c) != 'Mn')

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"