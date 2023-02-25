from math import pi


def area(self):
    return 4 * pi * self.radius ** 2


def print_area(self):
    print("the area is" + str(super().area()))