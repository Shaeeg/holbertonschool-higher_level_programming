#!/usr/bin/python3
"""Module that replaces an element of a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """Replace element at idx, or return original list if idx is invalid."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
