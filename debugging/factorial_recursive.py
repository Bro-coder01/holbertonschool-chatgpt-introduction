#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function description:
        Calculates the factorial of a non-negative integer recursively.

    Parameters:
        n (int): The number whose factorial will be calculated.

    Returns:
        int: The factorial value of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
