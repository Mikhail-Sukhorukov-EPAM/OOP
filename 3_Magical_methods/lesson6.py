"""3.6 Магический метод __bool__
Если нет __bool__ смотрит в __len__"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x - self.y

    def __bool__(self):
        return self.x != 0 or self.y != 0


"""
p1 = Point(0, 0)
print(bool(p1))
p2 = Point(1, 0)
print(bool(p2))

if p2:
    print("hello")
"""


class City:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return f"{self.name}"

    def __bool__(self):
        return self.name[-1] not in "aeiou"


"""
c1 = City("Moscow")
c2 = City("Mosco")
print(bool(c1))
print(bool(c2))
"""


class Quadrilateral:
    def __init__(self, width, height="dtdfdf"):
        self.width = width
        if isinstance(height, str):
            self.height = width
        else:
            self.height = height

    def __str__(self):
        return f"Куб размером {self.width}х{self.height}" if self.width == self.height \
            else f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.width == self.height


q3 = Quadrilateral(10, 0)
print(q3)
