#!/usr/bin/python3
"""
N queens
usage:
>> ./0-nqueens.py 4
>> [[0, 1], [1, 3], [2, 0], [3, 2]]
>> [[0, 2], [1, 0], [2, 3], [3, 1]]
"""
import sys


# correct number of arguments
if (len(sys.argv) != 2):
    print("Usage: nqueens N")
    exit(1)

# correct data type
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

# correct range of accepted values
if (n <= 4):
    print("N must be at least 4")
    exit(1)
