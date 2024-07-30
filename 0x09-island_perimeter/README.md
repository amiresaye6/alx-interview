# Island Perimeter

This repository contains the solution to the "Island Perimeter" problem.

## Problem Description

Given a 2D grid map of `1`s (land) and `0`s (water), compute the perimeter of the island. The grid is surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

## Solution

The solution to this problem can be implemented using a depth-first search (DFS) algorithm. By traversing the grid and counting the number of neighboring water cells for each land cell, we can calculate the perimeter of the island.

## Implementation

The solution is implemented in [island_perimeter.py](island_perimeter.py). The `islandPerimeter` function takes a 2D grid as input and returns the perimeter of the island.

To run the solution, execute the following command:

```
python island_perimeter.py
```

## Example

Input:
```
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

Output:
```
16
```
