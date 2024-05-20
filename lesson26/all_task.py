# Task 1
from typing import Optional

def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    """
    Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.
    """
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    if exp == 0:
        return 1
    return x * to_power(x, exp - 1)

# Task 2
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """
    if index >= len(looking_str) // 2:
        return True
    if looking_str[index] != looking_str[len(looking_str) - index - 1]:
        return False
    return is_palindrome(looking_str, index + 1)

# Task 3
def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
    """
    if n < 0:
        raise ValueError("This function works only with postive integers")
    if n == 0:
        return 0
    return a + mult(a, n - 1)

# Task 4
def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """
    if len(input_str) == 0:
        return input_str
    return reverse(input_str[1:]) + input_str[0]

# Task 5
def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
    """
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])
