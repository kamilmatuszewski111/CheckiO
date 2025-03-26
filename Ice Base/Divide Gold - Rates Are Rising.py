"""
 Captain Red Eye and his sailors luckily found another chest containing a large number of identical gold coins.
 To divide up the coins, the crew tried to use their previous rules:

    each sailor, except the Captain, should receive exactly the same number of coins;
    the Captain should receive twice as many coins as a sailor.

In case the coins cannot be divided evenly using this method, the Captain, being the only person with a gun on board,
decided to use his weapon effectively and mercifully - to minimally decrease the number of sailors to get an integer result of shares.

However, the sailors were not happy with such a prospect and secretly decided that if the given number of coins could
be evenly divided without the Captain's share, they would pounce and remove him from leadership.

So, the priority of checking cases should be the following:

    Captain's double share, no kills;
    The crew makes a riot against Captain;
    Captain starts to kill sailors;
    Captain kills all and take all gold.

Given the number of coins in the chest and the number of sailors, write a program to determine the best share Captain
or sailor (depending on suitable case) can receive.

Input: Two integers (int).

Output: Integer.
"""

def captain_kills(gold: int, sailors: int) -> int:
    response = gold if sailors < 1 else (gold/(2+sailors))
    if response.is_integer() and sailors > 0:
        return int(response*2)
    elif response.is_integer():
        return int(response)
    else:
        return captain_kills(gold, sailors-1)


def winner_share(gold: int, sailors: int) -> int:
    first_case = gold if sailors < 1 else (gold/(2+sailors))
    if first_case.is_integer() and sailors > 0:
        return int(2*first_case)
    elif first_case.is_integer():
        return int(first_case)
    elif gold % sailors == 0:
        return int(gold/sailors)
    elif captain_kills(gold, sailors):
        return captain_kills(gold, sailors)
    else:
        return gold
print("Example:")
print(winner_share(15, 1))

# These "asserts" are used for self-checking
assert winner_share(15, 4) == 6
assert winner_share(16, 4) == 4
assert winner_share(100, 11) == 20
assert winner_share(15, 1) == 10
assert winner_share(28, 2) == 14
assert winner_share(54, 4) == 18