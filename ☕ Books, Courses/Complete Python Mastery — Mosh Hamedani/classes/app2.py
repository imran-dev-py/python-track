class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.y

    def __str__(self):
        return f'({self.x}, {self.y})'


point = Point(10, 15)
point2 = Point(20, 25)

print(point + point2)  # 35
