#!/usr/bin/python3
"""Module that replaces an element in a copy of a list."""


def new_in_list(my_list, idx, element):
    """Replace element at idx in a copy, or return copy if idx is invalid."""
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
