#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Function to create a list of lists representing the Pascal's triangle of n
    Args:
        n (int): an integer
    Returns:
        matrix: a list of lists

    Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    Note: this approach uses nCr formula and factorial from math module
    """
    from math import factorial as fact

    # Outer loop iterates from 0 to n
    for i in range(n):
        # Inner loop iterates from 0 to i + 1
        for j in range(i + 1):
            # Apply nCr formula: nCr = n! / ((n - r)! * r!)
            # here n = i & r = j
            line = fact(i) // (fact(i - j) * fact(j))
            print(line, end='')
        # print a new line after each line
        print()
