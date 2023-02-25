import math


class cylinder:
    def _init_(self, radius, height):
        self.radius = radius
        self.height = height
    def volume(self):
        return math.pi * self.radius ** 2  * self.height