#author DMH 4/11/22

import math


class Circle:
    """ Circle class represents a circle """

    def __init__(self):
        """ Create a new circle with radius 3 """

        self.radius = 3

    def get_area(self):
        """ Calculate area of circle """

        return self.radius ** 2 * math.pi

my_circle = Circle()

print(my_circle.get_area())
