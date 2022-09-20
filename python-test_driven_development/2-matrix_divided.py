#!/usr/bin/python3
"""_summary_ module containing a function matrix_divided
"""


def matrix_divided(matrix, div):
    """function that divides all the elements of a matrix"""
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) != int and type(x) != float:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
    divided = [list(map(lambda x: round(x/div, 2), row)) for row in matrix]
    return divided
