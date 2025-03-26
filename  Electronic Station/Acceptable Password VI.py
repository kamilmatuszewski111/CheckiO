"""
 In this mission you need to create a password verification function.

The verification conditions are:

    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case;
    must contain at least 3 different (case-sensitive) letters (or digits) even if it is longer than 10

Input: A string (str).

Output: A logic value (bool).
"""


def is_acceptable_password(text: str) -> bool:
    a = []
    if len(text) <= 9:
        a.append(any([i.isdigit() for i in text]))
        a.append(any([i.isalpha() for i in text]))
        return all(a) and len(text) > 6 and 'password' not in text.lower() and len(set(text)) >= 3
    else:
        return 'password' not in text.lower() and len(set(text)) >= 3


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True