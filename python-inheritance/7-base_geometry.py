#!/usr/bin/python3
"""Module that defines a BaseGeometry class with validation."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raise an Exception indicating area() is not implemented.

        >>> bg = BaseGeometry()
        >>> bg.area()
        Traceback (most recent call last):
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        >>> bg = BaseGeometry()
        >>> bg.integer_validator("my_int", 12)
        >>> bg.integer_validator("name", "John")
        Traceback (most recent call last):
        TypeError: name must be an integer
        >>> bg.integer_validator("age", 0)
        Traceback (most recent call last):
        ValueError: age must be greater than 0
        >>> bg.integer_validator("distance", -4)
        Traceback (most recent call last):
        ValueError: distance must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
