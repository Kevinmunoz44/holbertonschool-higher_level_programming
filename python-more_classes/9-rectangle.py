#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Construct"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """Get Width"""
    @property
    def width(self):
        return self.__width

    """Set Width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """get Height"""
    @property
    def height(self):
        return self.__height

    """set Height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Define Area"""
    def area(self):
        return self.__width * self.__height

    """Define Perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    """Define print and string"""
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = str(self.print_symbol) * self.__width + "\n"
        rectangle *= self.__height - 1
        rectangle += str(self.print_symbol) * self.__width
        return rectangle

    """Define repr and eval"""
    def __repr__(self):
        return f"Rectangle(%d, %d)" % (self.width, self.height)

    """Delete dots ellipsis"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
