#!/usr/bin/python3
"""
This module defines a simple function to add two numbers.
"""


def add_numbers(a, b):
    """
    Adds two numbers together and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b


if __name__ == "__main__":
    # Test the add_numbers function
    result = add_numbers(3, 5)
    print("Result:", result)
