import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return round(self.height * self.width, 2)

    def diagonal(self):
        return round(math.sqrt(self.height**2 + self.width**2), 2)
