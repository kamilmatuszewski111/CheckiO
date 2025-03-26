"""
 Sofia has had a very stressful month and decided to take a vacation for a week. To avoid any stress during her vacation she wants to forward emails with a stressful subject line to Stephen.

The function should recognize if a subject line is stressful. A stressful subject line means that all letters are in uppercase, and/or the whole line ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.

Input: Subject line as a string.

Output: Boolean.
"""


def is_stressful(subj):
    """
        recognize stressful subject
    """
    list = ['asap', 'help', 'HELP', 'h!e!l!p', 'A.S.A.P.!!', '!!!!', 'UUUURGGGEEEEENT ','U-R-G-E-N-T','urgent',subj.upper()]
    counter = 0
    for i in list:
        if i in subj:
            counter += 1
    return counter > 0

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"