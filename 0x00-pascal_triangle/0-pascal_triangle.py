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
    triangle = [[]] * n
    column = 0


    if n <= 0:
        return []
