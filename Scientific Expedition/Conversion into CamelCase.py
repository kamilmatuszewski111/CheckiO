"""
 Your mission is to convert the name of a function from the Python format (for example "my_function_name") into CamelCase ("MyFunctionName") where the first char of every word is in uppercase and all words are concatenated without any intervening characters.

example

Input: A function name as a string (str).

Output: The same string (str), but in CamelCase.
"""


def to_camel_case(name: str) -> str:
    return ''.join([x.capitalize() for x in name.split('_')])


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"