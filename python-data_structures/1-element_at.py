#!/usr/bin/python3
"""Module that retrieves an element from a list."""


def element_at(my_list, idx):
    """Return element at idx, or None if idx is negative or out of range."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
