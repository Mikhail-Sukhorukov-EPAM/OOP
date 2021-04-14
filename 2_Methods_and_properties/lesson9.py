""" 2.9 Classmethod и staticmethod """


"""
class Example:
    def hello():
        print("hello")

    def instance_hello(self):
        print(f"instance_hello {self}")

    @staticmethod
    def staticmethod_hello():
        print(f"staticmethod_hello")

    @classmethod
    def classmethod_hello(cls):
        print(f"classmethod_hello {cls}")


Example.classmethod_hello()
Example.hello()
e1 = Example()
e1.instance_hello()
e1.staticmethod_hello()
"""


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")