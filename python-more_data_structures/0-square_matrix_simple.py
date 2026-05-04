#!/usr/bin/python3
"""Module that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared."""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
