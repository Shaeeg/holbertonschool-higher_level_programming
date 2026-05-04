#!/usr/bin/python3
"""Module that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary with keys sorted alphabetically."""
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
