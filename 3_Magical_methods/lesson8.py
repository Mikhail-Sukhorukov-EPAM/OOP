"""3.8 Полиморфизм в Python"""


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f"Circle radius = {self.r}"

    def get_area(self):
        return 3.14 * self.r ** 2


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"Square {self.a}x{self.a}"

    def get_area(self):
        return self.a ** 2


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Rectangle {self.a}x{self.b}"

    def get_area(self):
        return self.a * self.b


s1 = Square(8)
s2 = Square(4)

r1 = Rectangle(4, 5)
r2 = Rectangle(9, 6)

c1 = Circle(8)
c2 = Circle(4)

figures = [s1, s2, c1, c2, r1, r2]
for figure in figures:
    print(figure, figure.get_area())
