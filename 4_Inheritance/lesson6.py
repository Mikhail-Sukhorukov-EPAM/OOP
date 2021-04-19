""" 4.6 Множественное наследование """


class Doctor:
    def __init__(self, degree):
        self.degree = degree


class Builder:
    def __init__(self, rank):
        self.rank = rank


class Person(Builder, Doctor):
    def __init__(self, rank, degree):
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def __str__(self):
        return f"My rank is {self.rank}, my degree is {self.degree}"


p1 = Person(5, "master")
print(p1)
