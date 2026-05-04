#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line."""
    for row in matrix:
        print(" ".join("{:d}".format(n) for n in row))
