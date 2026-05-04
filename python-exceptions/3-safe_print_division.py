#!/usr/bin/python3
"""Module that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    """Divide a by b and print the result, returning it or None."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
