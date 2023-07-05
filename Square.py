import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side**2, 2)

    def diagonal(self):
        return round(math.sqrt((self.side**2) * 2), 2)
