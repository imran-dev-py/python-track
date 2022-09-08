class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        # V = πr^2h
        return (Cylinder.pi * pow(self.radius, 2) * self.height)

    def surface_area(self):
        # A = 2πrh+2πr^2
        A1 = (2 * Cylinder.pi * self.radius * self.height)
        A2 = (2 * Cylinder.pi * pow(self.radius, 2))
        return A1 + A2


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
