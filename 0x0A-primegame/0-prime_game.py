#!/usr/bin/python3
"""
This module contains functions related to a prime game.
"""


def isPrime(number: int) -> bool:
    """
    Check if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def isWinner(x: int, nums: list) -> str:
    """
    Determine the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): A list of numbers representing the rounds.

    Returns:
        str: The name of the winner ("Maria" or "Ben").
    """
    Maria = 0
    Ben = 0
    for round in nums:
        if round == 2:
            Maria += 1
            continue
        is_prime_counter = 0
        for i in range(2, round):
            if isPrime(i):
                is_prime_counter += 1

        if is_prime_counter % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Maria < Ben:
        return "Ben"
    return None
