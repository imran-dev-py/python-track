"""
when in a class only have attributes and no methods on it and perform some numeric operation
using nametuple instead of class [__eq__, __gt__], it's less code and easily understands
and namedtuple can't be set new value [immutable]
"""

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=5, y=3)
p2 = Point(x=4, y=2)
print(p1 == p2)  # False
print(p1 > p2)  # True
