"""3.1 Магические методы. Методы __str__ и __repr__"""


class User:
    users = []

    def __init__(self, user):
        self.user = user
        User.users.append(self.user)

    def __str__(self):
        # u1
        # < __main__.User object at 0x1085271f0 >
        # print(u1)
        # It is a user: Mikhail
        # str(u1)
        # 'It is a user: Mikhail'
        return f"It is a user: {self.user}"

    def __repr__(self):
        # u1
        # It is a user: Mikhail
        # print(u1)
        # It is a user: Mikhail
        # str(u1)
        # 'It is a user: Mikhail'
        return f"User: {self.user}, List of Users: {User.users}"


class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        self.my_gender = gender

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"

    @property
    def my_gender(self):
        return self.gender

    @my_gender.setter
    def my_gender(self, new_gender):
        if new_gender == "male":
            self.gender = new_gender
        elif new_gender == "female":
            self.gender = new_gender
        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"


"""
p1 = Person("Mikhail", "Sukhorukov", "male")
print(p1)
p2 = Person("Darya", "Motorina", "female")
print(p2)
p3 = Person("Darya", "Motorina", "fmale")
print(p3)
p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
"""


class Vector:
    def __init__(self, *args):
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)

    def __str__(self):
        if not self.values:
            return "Пустой вектор"
        else:
            return f"Вектор{(*sorted(self.values),)}"


v1 = Vector(4, 2, 3, 4, "Sdfasdf")
print(v1.values)
print(v1)
v2 = Vector("fasdf")
print(v2.values)
print(v2)
v3 = Vector()
print(v3.values)
print(v3)

