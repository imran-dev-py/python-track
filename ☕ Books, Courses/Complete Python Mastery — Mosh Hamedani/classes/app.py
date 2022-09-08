class Point():
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f'point ({self.x},{self.y})'


point = Point(45, 20)
print(point.draw())

point.default_color = 'yellow'
print(Point.default_color)  # yellow
print(point.default_color)  # red

another_point = Point(10, 5)
print(another_point.default_color)  # red