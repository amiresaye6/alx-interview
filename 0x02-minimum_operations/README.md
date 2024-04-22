# Tasks

## 0. Lockboxes

### Mandatory

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1`, and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

### Prototype:

???python
def canUnlockAll(boxes):
???

- `boxes` is a list of lists

### Rules:

- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have corresponding boxes.
- The first box `boxes[0]` is unlocked by default.

### Return:

- Return `True` if all boxes can be opened, else return `False`.

## 1. Minimum Operations

### Mandatory

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` H characters in the file.

### Prototype:

```python
def minOperations(n):
```

### Returns:

- An integer

### Example:

```python
n = 9

# H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

# Number of operations: 6
```

- If `n` is impossible to achieve, return `0`.
