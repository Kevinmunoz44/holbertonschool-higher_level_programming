#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[i - (j % 1) * (i + i + 1)][j], end=" ")
        print()