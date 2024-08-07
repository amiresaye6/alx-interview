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
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def my_sieve_of_eratosthenes(max_num: int) -> list:
    """
    Generate a list of booleans representing prime numbers up to max_num.

    Args:
        max_num (int): The maximum number to check for primes.

    Returns:
        list: A list where True indicates a prime number.
    """
    primeLits = [True] * (max_num + 1)
    primeLits[0], primeLits[1] = False, False
    for num in range(2, max_num + 1):
        if primeLits[num]:
            primeLits[num] = isPrime(num)
    return primeLits


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
    is_prime = my_sieve_of_eratosthenes(max_num)

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
