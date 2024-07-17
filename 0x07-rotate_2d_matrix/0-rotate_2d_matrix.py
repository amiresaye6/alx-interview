#!/usr/bin/python3
"""
Rotate 2D matrix of n by n dimentions module
"""


def swap_helper(a: int, b: int) -> list:
    """
    Swaps the values of two numbers in place without using an extra variable.

    Args:
        a (int): The first number to swap.
        b (int): The second number to swap.

    Returns:
        None. The function modifies the values of the input variables directly.

    """
    a = a + b
    b = a - b
    a = a - b
    return [a, b]


def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix 90 degrees clockwise.

    This function takes a square matrix (2D list) as input and rotates it
    in-place, meaning the matrix is directly modified without using extra
    space for another matrix.

    Parameters:
    - matrix (list of list of int): The 2D matrix to be rotated.

    Returns:
    None. The input matrix is modified in-place.

    Example:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        rotate_2d_matrix(matrix)
        # Now matrix is:
        # [
        #   [7, 4, 1],
        #   [8, 5, 2],
        #   [9, 6, 3]
        # ]
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    [matrix[i].reverse() for i in range(n)]
