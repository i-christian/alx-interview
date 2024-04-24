#!/usr/bin/python3
"""
Rotate 2D Matrix

This module provides a function to rotate a
two-dimensional matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a two-dimensional matrix 90 degrees clockwise in place.

    Args:
        matrix (list of lists): The matrix to be rotated.

    Returns:
        None. The matrix is rotated in place.
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # current number
            tmp = matrix[i][j]
            # change top for left
            matrix[i][j] = matrix[x][i]
            # change left for bottom
            matrix[x][i] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = tmp
