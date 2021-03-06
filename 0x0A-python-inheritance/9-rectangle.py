#!/usr/bin/python3
"""Creates a class named BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class"""
    def __init__(self, width, height):
        """initialize"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area"""
        return self.__width * self.__height

    def __str__(self):
        """string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
