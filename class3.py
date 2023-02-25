from kk import circle
from math import pi

class Ball (circle):
    def valume(self):
        v=(4/3)*pi*self.radius
        return v

    def area(self):
        return 4 *pi * self.radius**2

    def print_area(self):
        print("the area is"+str().area())