#!/usr/bin/python3
"""2-rectangle.py"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Creates an instance of Rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the value of private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the value of private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """public instance area"""

        return self.width * self.height

    def perimeter(self):
        """public instance method perimeter of a rectangle"""

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)
