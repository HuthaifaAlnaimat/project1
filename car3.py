class circle:
    def _init_(self, radius):
        self.radius = radius


    def area(self):
        area = self.radius ** 2 * 3.14
        return area


c1 = circle(5)
c2 = circle(10)
print(c1.area())