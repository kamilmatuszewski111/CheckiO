"""
 Your mission is to convert the name of a function from CamelCase ("MyFunctionName") into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".

example

Input: A function name as a CamelCase string (str).

Output: The same string (str), but in under_score.
"""


def from_camel_case(name: str) -> str:
    a = ''
    for i in name:
        if i.isupper():
            a += f'_{i}'
        else:
            a += i
    return a.lstrip('_').lower()


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"