#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> rotate_2d_matrix(matrix)
>>> print(matrix)
>>> [
...     [7, 4, 1],
...     [8, 5, 2],
...     [9, 6, 3]
... ]
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D Matrix.
    Rotate it 90 degrees clockwise in place.

    :param matrix: n x n 2D matrix
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i].reverse()
