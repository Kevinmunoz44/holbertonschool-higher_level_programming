#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            """si not of type int raises TypeError"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """de lo contrario raise valueError"""
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            position (tuple): The new position of the square.
                              Should be a tuple of 2 positive integers.
        """
        # if not isinstance(value, tuple) or len(value) != 2:
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Get the area of the square

        returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character and position."""
        if self.__size == 0:
            """
            if not is zero imprime space
            """
            print()
        else:
            for _ in range(self.__position[1]):
                """ positon[1] imprime space"""
                print()
            for _ in range(self.__size):
                """ if size position[0], imprime  # """
                print(" " * self.__position[0] + "#" * self.__size)
