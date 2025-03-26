"""
 Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, he is more careful in the presence of such sophisticated characters ([Shift] + [a]) and will press the keys correctly.) Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the letter keys “a” and “z”, and has no effect on the other keys or characters. The “Caps Lock” key is assumed to be initially off.

For Joe's keyboard, Caps Lock always uppercases a letter. That means if Caps Lock is on, and Joe does Shift + b, 'B' (in upper case) gets printed.

Input: A string (str). The typed text.

Output: A string (str). The resulting text after being typed.
"""


def caps_lock(text: str) -> str:
    kupa = ""
    flag = False
    for i in text:
        if i == 'a':
            flag = True if flag == False else False
        if flag:
            kupa += i.upper()
            kupa = kupa.rstrip("A")
            kupa = kupa.rstrip("a")
        else:
            kupa += i
            if i == "A":
                pass
            else:
                kupa = kupa.rstrip("A")
                kupa = kupa.rstrip("a")
    return kupa


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"