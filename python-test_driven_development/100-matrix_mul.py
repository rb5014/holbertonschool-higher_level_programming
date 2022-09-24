#!/usr/bin/python3
"""module containing the function matrix_mul
"""


def matrix_mul(m_a=[[1]], m_b=[[1]]):
    """_summary_ - multiplies 2 matrices

    Args:
        m_a (_type_): must be list of integers or float
        m_b (_type_): must be list of integers or float
        m_a and m_b must be an list of lists of integers or floats:

if m_a or m_b is not a list: raise a TypeError exception with the
 message m_a must be a list or m_b must be a list

if m_a or m_b is not a list of lists: raise a TypeError exception with the
 message m_a must be a list of lists or m_b must be a list of lists

if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError
 exception with the message m_a can't be empty or m_b can't be empty

if one element of those list of lists is not an integer or a float: raise a
 TypeError exception with the message m_a should contain only integers or
  floats or m_b should contain only integers or floats

if m_a or m_b is not a rectangle (all 'rows' should be of the same size):
 raise a TypeError exception with the message each row of m_a must be of the
  same size or each row of m_b must be of the same size

If m_a and m_b can’t be multiplied: raise a ValueError exception with the
 message m_a and m_b can't be multiplied
    """
    #                           #
    # Requirements checked here #
    #                           #

    # is list?
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    # is list of lists?
    if not all(isinstance(x, list) for x in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError('m_b must be a list of lists')
    # is empty?
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    # all int or float?
    for i in range(len(m_a)):
        if not all(isinstance(x, (int, float)) for x in m_a[i]):
            raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        if any(isinstance(x, (int, float)) is False for x in row):
            raise TypeError('m_b should contain only integers or floats')
    # is rectangle?
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for i in m_b:
        if len(i) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
    # nb columns m_a == nb rows m_b ?
        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    #               #
    # Multiplication
    #               #

    # Initialisation of new matrix
    new_rows = len(m_a)
    new_cols = len(m_b[0])
    mul_ab = [[0 for i in range(new_cols)] for j in range(new_rows)]
    # loop for rows
    for i in range(new_rows):
        # loop for columns
        for j in range(new_cols):
            # loop for multiplication
            for k in range(len(m_b)):
                mul_ab[i][j] += m_a[i][k] * m_b[k][j]
    return mul_ab
