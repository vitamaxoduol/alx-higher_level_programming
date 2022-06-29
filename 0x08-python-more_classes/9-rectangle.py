#!/usr/bin/python3
"""9-rectangle.py"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Creates an instance of Rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Finds the area of the Rectangle
        Returns: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Finds the perimeter of the Rectangle
        Returns: perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of a rectangle """
        if self.width == 0 or self.height == 0:
            return ""

        symbol = str(self.print_symbol)
        result = [symbol * self.width for i in range(self.height)]
        return "\n".join(result)

    def __repr__(self):
        """Internal representation of a rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes an instance of a Rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Finds the larger rectangle between 2 rectangles based on area
        Args:
            rect_1: 1st rectangle
            rect_2: 2nd rectangle
        Return: The larger rectangle or rect_1 if the areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square of a given size
        Args:
            size: length oof one side of the square
        Returns:
            a new Rectangle instance with width == height == size
        """
        return Rectangle(size, size)
