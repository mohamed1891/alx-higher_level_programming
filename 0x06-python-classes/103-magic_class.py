#!/usr/bin/python3

import math


class MagicClass:
    def __init__(self, radius):
        self.__radius = 0  # Initialize __radius attribute with 0
        
        # Check if radius is either int or float, otherwise raise TypeError
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        
        self.__radius = radius  # Set __radius if radius is valid

    def area(self):
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
