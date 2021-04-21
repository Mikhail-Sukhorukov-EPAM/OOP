""" 3.7 Slots
slots быстрееб строгое число атрибутов экземпляра """


class Point:
    "Тут можно добавать другие атрибуты экземпляра"

    def __init__(self, x, y):
        self.x = x
        self.y = y


class SlotsPoint:
    "Тут все возможные атрибуты экземпляра класса предоставлены в виде коллекции __slots__ "
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(0, 8)
s1 = SlotsPoint(8, 5)
p1.z = 8
s1.z = 8
