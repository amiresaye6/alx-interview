#!/usr/bin/python3
"""
task: 0. Lockboxes
condition: mandatory
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    You have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and may contain keys to other boxes.

    Args:
        boxes (List[List[int]]): A list of lists where each inner list
        contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Notes:
        - A key with the same number as a box opens that box.
        - All keys will be positive integers.
        - There can be keys that do not have corresponding boxes.
        - The first box, boxes[0], is unlocked by default.
    """
    keyes = boxes[0]
    boxes[0] = True

    for key in keyes:
        try:
            if boxes[key] is True:
                continue
            keyes += boxes[key]
            boxes[key] = True
        except IndexError:
            continue

    for val in boxes:
        if val is not True:
            return False
    return True
