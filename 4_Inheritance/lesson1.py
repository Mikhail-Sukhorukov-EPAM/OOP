""" 4.1 Принцип наследования в ООП
и так это знаю
"""


class Human:
    def can_walk(self):
        print("I am walking")


class Doctor(Human):
    def can_heal(self):
        print("I am healing")


class Teacher(Human):
    def can_teach(self):
        print("I am teaching")


t1 = Teacher()
t1.can_walk()
t1.can_teach()

d1 = Doctor()
d1.can_walk()
d1.can_heal()
