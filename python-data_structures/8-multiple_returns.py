#!/usr/bin/python3
"""Module that returns a tuple with length and first character of a string."""


def multiple_returns(sentence):
    """Return a tuple with the length and first character of a string."""
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
