from math import pi
class circle:
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        area = self.radius ** 2 * pi
        return area

    def circ(self):
        circ = self.radius * 2 * pi
        return circ


c1 = circle(5)
c2 = circle(10)
print(c1.area())