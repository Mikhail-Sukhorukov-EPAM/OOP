"""
3.4 Специальные методы сравнения объектов классов
__eq__ - ==
__ne__ - !=
__lt__ - <
__le_- - <=
__gt__ = >
__ge__ = >=
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, tuple)):
            return self.area < other

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area > other.area
        elif isinstance(other, (int, tuple)):
            return self.area > other

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


r1 = Rectangle(1, 2)
r2 = Rectangle(2, 1)
r3 = Rectangle(5, 8)
r4 = Rectangle(2, 1)
print(r1 == r2)
print(r2 == r1)
print(r2 == r3)
print(r1 == r3)
print(r1 < r3)
print(r2 < r3)
print(r3 < r1)
print(r2 == r4)
print(1 < r1)
print(1 != r1)
