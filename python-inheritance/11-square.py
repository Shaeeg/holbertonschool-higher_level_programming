#!/usr/bin/python3
"""Module that defines a Square class with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
