#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i in range(0, len(x)):
            print("{:d}".format(x[i]), end="")
            if i < len(x) - 1:
                print(" ", end="")
        print()
