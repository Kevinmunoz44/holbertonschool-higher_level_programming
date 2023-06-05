#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for k, j in enumerate(i):
            if k != len(i) - 1:
                print(j, end=" ")
            else:
                print('{:d}'.format(j), end="")
        print()
