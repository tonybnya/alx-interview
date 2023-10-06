#!/usr/bin/python3
"""
Lockboxes

You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
  - There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and each box
    may contain keys to the other boxes.

    Function that determines if all the boxes can be opened.
    Args:
        boxes (matrix): a list of lists of positive integers
    Returns:
        boolean

    Examples:
        >>> boxes = [[1], [2], [3], [4], []]
        >>> canUnlockAll(boxes)
        >>> True

        >>> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        >>> canUnlockAll(boxes)
        >>> True

        >>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        >>> canUnlockAll(boxes)
        >>> False

    Time Complexity:
    Space Complexity:
    """
    hashmap = {0: boxes[0]}
    visited = set()

    for i in range(len(boxes)):
        if i in hashmap:
            visited.add(i)
            for item in hashmap[i]:
                if item in hashmap:
                    continue
                else:
                    hashmap[item] = boxes[item]
        else:
            hashmap[i] = boxes[i]

    return len(boxes) == len(visited)
