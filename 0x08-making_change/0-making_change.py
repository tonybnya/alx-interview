#!/usr/bin/python3
"""
Change comes from within

Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`
    - If `total` is `0` or less, return `0`
    - If `total` cannot be met by any number of coins you have, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination of coin
  in the list
- Your solution’s runtime will be evaluated in this task

Examples:

    >>> coins = [1, 2, 25]
    >>> total = 37
    >>> print(makeChange(coins, total))
    >>> 7
    >>>
    >>> coins = [1256, 54, 48, 16, 102]
    >>> total = 1453
    >>> print(makeChange(coins, total))
    >>> -1
"""


def makeChange(coins, total):
    """
    Main function

    :param coins: a list of integers
    :param total: an integer
    :return: an integer
    """
    if total <= 0:
        return 0

    # TC: O(nlogn) - SP: O(n)
    coins_sorted: List[int] = sorted(coins, reverse=True)
    n: int = len(coins_sorted)

    counter: int = 0
    i: int = 0
    while total > 0:
        if i >= n:
            return -1

        if total - coins_sorted[i] >= 0:
            total -= coins_sorted[i]
            counter += 1
        else:
            i += 1

    return counter
