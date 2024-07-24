# README

This is the README file for the `0x08-making_change` project.

## Description

The `0x08-making_change` project is a coding exercise that focuses on implementing an algorithm to make change using the minimum number of coins.

## Files

The project consists of the following files:

- `0-make_change.py`: Contains the implementation of the `make_change` function.

## Usage

To use the `make_change` function, follow these steps:

1. Import the function: `from 0-make_change import make_change`
2. Call the function with the desired amount: `make_change(amount)`

## Example

```python
from 0-make_change import make_change

amount = 67
result = make_change([25, 10, 5, 1], amount)
print(result)  # Output: [25, 25, 10, 5, 1, 1]
```
