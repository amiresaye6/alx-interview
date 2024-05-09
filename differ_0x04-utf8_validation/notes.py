#!/usr/bin/python3
"""
task: 0. UTF-8 Validation

condition: mandatory

required:
Write a method that determines if a given data set represents a valid UTF-8
encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the
least significant bits of each integer
"""
from typing import List

def validUTF8(data: List[int]):
    """
    determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list(int)): list of data to check

    Return:
        true if the data is utf-8 encoded or false if not
    """
    pinary_data = [bin(num) for num in data]
    return pinary_data



number = 10
binary_representation = format(number, '08b')  # Pad with leading zeros to make it 8 digits long
print(binary_representation)  # Output: '00001010'
# test code

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
