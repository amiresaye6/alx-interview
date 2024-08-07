#!/usr/bin/python3
"""
This module contains functions related to a prime game.
"""


def sieve_of_eratosthenes(max_num: int) -> list:
    """
    Generate a list of booleans representing prime numbers up to max_num.

    Args:
        max_num (int): The maximum number to check for primes.

    Returns:
        list: A list where True indicates a prime number.
    """
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for start in range(2, int(max_num**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, max_num + 1, start):
                is_prime[multiple] = False

    return is_prime


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of numbers representing the rounds.

    Returns:
        str: The name of the winner ("Maria" or "Ben").
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    is_prime = sieve_of_eratosthenes(max_num)

    Maria = 0
    Ben = 0

    for n in nums:
        prime_count = sum(is_prime[2:n+1])
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
