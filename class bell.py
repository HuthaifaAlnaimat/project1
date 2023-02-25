from cmath import pi


class ball:
    def _init_(self, radius, height):
        self.radius = radius

    def volume(self):
        v = (3 / 4) * pi * self.radius ** 3
        return v