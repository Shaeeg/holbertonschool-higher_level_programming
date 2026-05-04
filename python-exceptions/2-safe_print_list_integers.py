#!/usr/bin/python3
"""Module that prints the first x integers of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print first x integers of a list, skip non-integers silently."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
