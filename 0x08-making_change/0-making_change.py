#!/usr/bin/python3
"""
For the “0. Change comes from within” project, you will tackle a classic
problem from the domain of dynamic programming and greedy algorithms: the
coin change problem. The objective is to find the minimum number of coins
required to make up a given total amount, given a list of coin denominations.
This project challenges you to apply your understanding of algorithms to devise
a solution that is not only correct but also efficient. Below are the key
concepts and resources necessary to complete this project successfully.
"""


def makeChange(coins: list, total: int) -> int:
    """
    Calculates the minimum number of coins required to make up a given total
    amount.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount to be made up.

    Returns:
        int: The minimum number of coins required.

    """
    if total <= 0:
        return 0

    min_value = min(coins)
    if min_value > total:
        return -1

    # print(coins)
    coins.sort(reverse=True)
    # print(coins)
    temp = 0
    i = 0
    c = 0
    coins_length = len(coins)

    while temp < total:
        temp += coins[i]
        c += 1
        if temp > total:
            temp -= coins[i]
            c -= 1
            i += 1
            if i == coins_length:
                return -1
        elif temp == total:
            return c
