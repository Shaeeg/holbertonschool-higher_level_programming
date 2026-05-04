#!/usr/bin/python3
"""Module that defines a Student class with filtered to_json method."""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation, filtered by attrs if provided."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
