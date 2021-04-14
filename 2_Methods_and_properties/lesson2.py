"""2.2 Инициализация объекта. Метод init"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def is_adult(self):
        return False if self.age < 18 else True


class Zebra:
    def __init__(self):
        self.count_of_stripe = 0

    def which_stripe(self):
        if self.count_of_stripe % 2 == 0:
            print("Полоска белая")
        else:
            print("Полоска черная")
        self.count_of_stripe += 1


class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"


laptop1 = Laptop("asus", "111", 123)
laptop2 = Laptop("hp", "fgf", 555)