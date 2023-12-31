#!/usr/bin/python3
"""
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

    >>> print(makeChange([1, 2, 25]), 37)
    >>> 7
    >>>
    >>> print(makeChange([1256, 54, 48, 16, 102], 1453)
    >>> -1
    >>> print(makeChange([186, 419, 83, 408], 6249)
    >>> 20
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Find the fewest number of coins needed to meet the given total.

    :param coins: a list of integers
    :param total: an integer
    :return: an integer

    Time Complexity: O(nlogn + total)
    Space Complexity: O(1) - the coins array has been sorted in place
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    # TC: O(nlogn) - SP: O(1)
    coins.sort(reverse=True)
    num_coins: int = len(coins)

    fewest_number_coins: int = 0
    index: int = 0
    while total > 0:  # O(total)
        if index >= num_coins:
            return -1

        coin = coins[index]
        if total - coin >= 0:
            total -= coin
            fewest_number_coins += 1
        else:
            index += 1

    return fewest_number_coins
