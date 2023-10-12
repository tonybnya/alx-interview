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

    Time Complexity: O(n + m)
    Space Complexity: O(n)
    """
    n = len(boxes)
    unlocked = [False] * n

    unlocked[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)

        for key in boxes[box]:
            if not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
