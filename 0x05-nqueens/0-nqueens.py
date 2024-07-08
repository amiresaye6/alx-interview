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
if (n < 4):
    print("N must be at least 4")
    exit(1)

def creat_board(n: int) -> list:
    """
    Create a 2D array representing a chessboard of size n x n.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A 2D array representing the chessboard.

    """
    return [[0 for _ in range(n)] for x in range(n)]


def check_safe_place(board: list, row: int, col: int, n: int):
    """
    Check if a queen can be placed on board[row][col].

    Args:
        board (list): The chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if the queen can be placed, False otherwise.

    """
    if (board[row][col]):
        return False
