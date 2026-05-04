#!/usr/bin/python3
"""Module that prints an integer with try/except."""


def safe_print_integer(value):
    """Print an integer and return True, or return False if not an integer."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
