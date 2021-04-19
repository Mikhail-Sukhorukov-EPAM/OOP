""" 4.5 Делегирование в Python """


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age


p1 = Person("Mikhail", "Sukhorukov")
d1 = Doctor("Ivan", "Petrov", 26)
print(p1.name, p1.surname)
print(d1.name, d1.surname, d1.age)
