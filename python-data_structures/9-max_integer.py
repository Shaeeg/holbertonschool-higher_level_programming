#!/usr/bin/python3
"""Module that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """Return the biggest integer in the list, or None if empty."""
    if len(my_list) == 0:
        return None
    maximum = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maximum:
            maximum = my_list[i]
    return maximum
