#!/usr/bin/python3
"""This is an empty rectangle class"""


class Rectangle:
    """This is a class"""
    def __init__(self, width=0, height=0):
        """Sets sizes"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Property"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
