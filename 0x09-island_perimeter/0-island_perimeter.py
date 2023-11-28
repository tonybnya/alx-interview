#!/usr/bin/python3
"""
Island Perimeter

Create a function `def island_perimeter(grid):`
that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes”
(water inside that isn’t connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    Island Perimeter

    :param grid: a list of list of integers
    :return: an integer as the perimeter
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Assuming all 4 sides are initially counted
                perimeter += 4

                # Check and subtract for adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtract 2 for the shared edge with the upper cell
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Subtract 2 for the shared edge with the left cell
                    perimeter -= 2

    return perimeter
