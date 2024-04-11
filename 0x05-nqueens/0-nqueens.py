#!/usr/bin/python3
"""Module for solving the N queens problem."""

import sys


def queens(n, i=0, a=[], b=[], c=[]):
    """Generate possible positions for placing queens on an N×N chessboard.

    Args:
        n (int): The size of the chessboard.
        i (int): The current row being evaluated.
        a (list): A list of column indices where queens are placed in each row.
        b (list): A list of diagonal positions where queens are placed.
        c (list): A list of diagonal positions where queens are placed.

    Yields:
        list: A valid solution with the positions of queens.

    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """Print all possible solutions for the N queens problem.

    Args:
        n (int): The size of the chessboard.

    """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve(N)
