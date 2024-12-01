class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def perimeter(self):
        return self.x + self.y + self.z


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
