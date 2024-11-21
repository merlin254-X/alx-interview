#!/usr/bin/python3
"""
This script performs a 90-degree rotation on a 2D matrix in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list[int]]): A 2D list (matrix) of integers.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
