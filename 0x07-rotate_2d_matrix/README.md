# README

This repository contains a file `0-rotate_2d_matrix.py` that implements the `rotate_2d_matrix(matrix)` function. This function is designed to rotate a 2D matrix of size `n` by `n`.

## Function Description

The `rotate_2d_matrix(matrix)` function takes a 2D matrix as input and rotates it 90 degrees clockwise. The input matrix is modified in-place, meaning that no additional space is used.

## Parameters

- `matrix`: A 2D matrix of size `n` by `n`.

## Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

# After rotation, the matrix becomes:
# [
#    [7, 4, 1],
#    [8, 5, 2],
#    [9, 6, 3]
# ]
```

## Constraints

- The input matrix will always be a square matrix of size `n` by `n`.
