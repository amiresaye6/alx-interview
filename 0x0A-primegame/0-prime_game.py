#!/usr/bin/env python3
"""
stuff for now
"""


def isPrime(number: int) -> bool:
    """
    stuff for now
    """
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def isWinner(x: int, nums: list) -> None:
    """
    stuff for now
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
        return("Maria")
    elif Maria < Ben:
        return("Ben")
    return None
