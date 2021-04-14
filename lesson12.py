""" 2.8 Вычисляемые свойства """


class Square:
    def __init__(self, side):
        self.__side = side
        self.__area = None
        self.__perimeter = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        self.__side = new_side
        self.__area = None
        self.__perimeter = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side ** 2
        return self.__area

    @property
    def perimeter(self):
        if self.__perimeter is None:
            self.__perimeter = self.side * 4
        return self.__perimeter

    def __str__(self):
        return f"Side is {self.side} meters, perimeter is {self.perimeter} meters, area is {self.area} square meters"
