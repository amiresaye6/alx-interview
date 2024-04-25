#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number `n`, write
a method that calculates the fewest number of operations needed to result in
exactly `n` H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly
    n 'H' characters in the file.

    Parameters:
    - n (int): The target number of 'H' characters to achieve in the file.

    Returns:
    - int: Returns the minimum number of operations needed to achieve n 'H'
    characters. If n is impossible to achieve, returns 0.

    Example:
    >>> minOperations(9)
    6

    - The sequence of operations to achieve 9 'H' characters:
    H => Copy All => Paste => HH => Paste => HHH =>
    Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
    """
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
