#!/usr/bin/python3
# 0-nqueens.py
# @tonybnya
"""The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
Write a program that solves the N queens problem.

Examples:

    julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
    julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
    julien@ubuntu:~/0x08. N Queens$
"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """find possible positions"""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """solve"""
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(n)


# def nqueens(N):
#     """Solves the N queens puzzle"""
#     col = set()
#     posDiag = set()
#     negDiag = set()
#
#     board = []
#
#     def backtrack(r):
#         if r == N:
#             return
#
#         for c in range(N):
#             if c in col or (r + c) in posDiag or (r - c) in negDiag:
#                 continue
#
#             col.add(c)
#             posDiag.add(r + c)
#             negDiag.add(r - c)
#             board.append([r, c])
#
#             backtrack(r + 1)
#
#             col.remove(c)
#             posDiag.remove(r + c)
#             negDiag.remove(r - c)
#             # pos = []
#
#     backtrack(0)
#
#     return board
#
#
# if __name__ == '__main__':
#     # If the user called the program with the wrong number of arguments
#     if len(sys.argv) != 2:
#         print('Usage: nqueens N')
#         sys.exit(1)
#
#     N = int(sys.argv[1])
#
#     # Check if N is an integer
#     if not isinstance(N, int):
#         print('N must be a number')
#         sys.exit(1)
#
#     # Check if N is at least 4
#     if N < 4:
#         print('N must be at least 4')
#         sys.exit(1)
#
#     board = nqueens(N)
#     # print(positions)
#
#     for pos in board:
#         print(pos)
