#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Prime Game
    Determine who the winner of each game

    :param x: an integer representing the number of rounds
    :param nums: an array of integers
    :return: the name of the winner or None
    """
    if x < 1 or not nums:
        return None

    maria, ben = 0, 0

    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben += primes_count % 2 == 0
        maria += primes_count % 2 == 1

    if maria == ben:
        return None

    return 'Maria' if maria > ben else 'Ben'
