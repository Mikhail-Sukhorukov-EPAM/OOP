""" 3.10 Магические методы __iter__ и __next__ """


class Person:
    def __init__(self, name="Mikhail", surname="Sukhorukov", age=24):
        self.list = [name, surname, age]
        self.index = 0

    def __iter__(self):
        print("call __iter__")
        return self

    def __next__(self):
        print("call __next__")
        if self.index == len(self.list):
            raise StopIteration
        self.value = self.list[self.index]
        self.index += 1
        return self.value


p1 = Person()
for i in p1:
    print(i)
