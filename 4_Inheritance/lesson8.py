""" Slots - нследование и property """


class Rectangle:
    __slots__ = "__height", "width"

    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height


r1 = Rectangle(8, 5)
r1.height = 10
print(r1.height)


class ColoredRectangle(Rectangle):
    """ список допустимых атрибутов экзепляра рсширяется на значение color для этого класса """
    __slots__ = "color"

    def __init__(self, height, width, color):
        super().__init__(height, width)
        self.color = color


c2 = ColoredRectangle(8, 5, "red")
c2.color = "blue"
print(c2.color)
