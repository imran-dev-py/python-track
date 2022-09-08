
class Circle():
    # Class object attribute
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_circle(self):
        return pow(self.radius, 2) * Circle.pi


circle = Circle(2)
print(circle.get_circle())
