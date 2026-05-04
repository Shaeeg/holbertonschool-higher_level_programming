#!/usr/bin/python3
"""Module that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    """Return a list of True/False whether each element is divisible by 2."""
    return [n % 2 == 0 for n in my_list]
