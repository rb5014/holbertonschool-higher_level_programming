#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = '\n'.join([' '.join(['{:d}'.format(i) for i in row])
                   for row in matrix])
    print(x)
