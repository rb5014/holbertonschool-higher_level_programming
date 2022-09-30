#!/usr/bin/python3
"""module containing the function pascal_triangle
"""


def pascal_triangle(n):
    """ that returns a list of lists of integers
    representing the Pascal’s triangle of n:

    Args:
        n (_type_): always integer
        returns empty list if n <= 0
    """
    mat = [[1 for x in range(row + 1)] for row in range(n)]
    for row in range(n):
        for i in range(row + 1):
            if i - 1 >= 0 and i + 1 < row + 1:
                mat[row][i] = sum(mat[row-1][i-1: i+1])

    return mat
