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
    num_bytes = 0

    # Masks to check the leading byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    # For each integer in the data
    for byte in data:
        # Check only the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte characters
            if num_bytes == 0:
                continue

            # Invalid scenarios
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For n bytes character,
            # the next bytes must be of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining in the current character
        num_bytes -= 1

    # All characters must be fully matched
    return num_bytes == 0
