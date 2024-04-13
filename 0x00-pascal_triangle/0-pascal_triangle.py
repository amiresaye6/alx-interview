#!/usr/bin/python3
"""
Module overview:
    this moduel has one function called pascal_triangle,
    this function accepts one parameter n,
    returns a two dimentional array.
"""


def pascal_triangle(n):
    """
    pascal_triangle: creats a pascal triangle using n
    n: input parameter userd to create the triangle >> int

    returns: two dimentional array(pascal triangel) or [] if failed.
    """
    triangle = [[1]]

    if n <= 0:
        return []

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
