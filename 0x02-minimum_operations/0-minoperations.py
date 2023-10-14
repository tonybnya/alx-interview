#!/usr/bin/python3
"""
Minimum Operations

In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0

Examples:
    >>> n = 9
    >>> minOperations(n)
    >>> 6

    >>> n = 4
    >>> minOperations(n)
    >>> 4

    >>> n = 12
    >>> minOperations(n)
    >>> 7
"""


def minOperations(n):
    """
    Function that calculates the minimum number of operations.

    Args:
        n (int): an integer as number of H to write
    Returns:
        an integer

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    # Check if n is 0 or 1
    # no operations are needed in these cases
    if n <= 1:
        return 0

    # # Create an array to store the minimum operations for each number
    # operations = [0] * (n + 1)
    #
    # for i in range(2, n + 1):
    #     # Initialize operations for i to be i operations
    #     operations[i] = i
    #
    #     for j in range(2, (i // 2) + 1):
    #         if i % j == 0:
    #             # If i is divisible by j, we can try to copy j times
    #             # and then paste the result, which takes two operations.
    #             operations[i] = min(operations[i], operations[j] + (i // j))

    # Initialize the number of operations
    operations = 0

    for i in range(2, n + 1):
        while n % i == 0:
            # If i is a divisor of n, repeatedly perform 'Copy All' and 'Paste'
            n //= i
            operations += i

    return operations
