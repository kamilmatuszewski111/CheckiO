"""
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
For example, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and their sum is 28.
"""


def is_perfect(n: int) -> bool:
    return True if sum([i for i in range(n)[1:] if not n % i]) == n else False


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False
