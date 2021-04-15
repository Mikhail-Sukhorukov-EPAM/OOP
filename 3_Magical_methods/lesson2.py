"""3.2 Магические методы __len__ и __abs__"""


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


class Otrezok:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def __len__(self):
        return abs(self)  # self.__abs__

    def __abs__(self):
        return abs(self.second_point-self.first_point)


o1 = Otrezok(2, 8)
print(len(o1))
print(abs(o1))

o2 = Otrezok(9, 5)
print(len(o2))
print(abs(o2))
