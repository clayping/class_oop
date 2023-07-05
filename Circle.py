import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.radius**2 * math.pi, 2)

    def perimeter(self):
        return round(self.radius * 2 * math.pi, 2)
