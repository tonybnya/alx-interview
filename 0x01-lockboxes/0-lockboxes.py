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
    # Get the length of the boxes as a variable n
    n = len(boxes)
    # Create a set to track the boxes we can open
    keys = set()
    # Start with the first box already opened
    keys.add(0)

    # Create a list to keep track of boxes that need to be checked
    queue = [0]

    # Traverse the boxes
    while queue:
        # Dequeue a box
        box = queue.pop()
        # For each key in the current box
        for key in boxes[box]:
            # Check if the key is a valid key
            # i.e. less than the the number of boxes
            # means that 0 <= key <= n - 1,
            # and if the key is not already in the set
            if key < n and key not in keys:
                # Add the the current key to the set
                keys.add(key)
                # Add the current to the list that keeping track
                # of the boxes needed to be checked
                queue.append(key)

    # Check if we can open all the boxes
    return len(keys) == n
