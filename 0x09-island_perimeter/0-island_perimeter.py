#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an
island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list): A 2D grid representing the island,
        where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.

    Example:
        >>> grid = [[0, 1, 0, 0],
        ...         [1, 1, 1, 0],
        ...         [0, 1, 0, 0],
        ...         [1, 1, 0, 0]]
        >>> island_perimeter(grid)
        16
    """
    width = len(grid[0])
    height = len(grid)
    p = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                if (
                    (j + 1 == width or grid[i][j + 1] == 0) and
                    (j - 1 < 0 or grid[i][j - 1] == 0) and
                    (i + 1 == height or grid[i + 1][j] == 0) and
                    (i - 1 < 0 or grid[i - 1][j] == 0) and
                    ((i + 1 < height and j + 1 < width) or grid[i + 1][j + 1] == 1)
                ):
                    continue
                if j + 1 == width or grid[i][j + 1] == 0:
                    p += 1
                    # print("found side cell: ({}, {})".format(i, j))
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    p += 1
                    # print("found side cell: ({}, {})".format(i, j))
                if i + 1 == height or grid[i + 1][j] == 0:
                    p += 1
                    # print("found side cell: ({}, {})".format(i, j))
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    p += 1
                    # print("found side cell: ({}, {})".format(i, j))

    return p
grid = [
       [0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0]
   ]
print(island_perimeter(grid))
