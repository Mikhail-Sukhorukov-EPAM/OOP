"""
3.5 Магические методы __eq__ и __hash__
наличие метода __eq__ делает обект нехешируемым если не перепределен метод __hash__ внутри класса
хэшируемые объекты - неизменяемые, только они могут быть ключами словаря
"""


class Dog:
    def __init__(self, name="Mick", age=2):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, Dog) and self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.age, self.name))
