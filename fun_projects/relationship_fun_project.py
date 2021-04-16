class Person:
    couples = []
    friends = []

    def __init__(self, name, surname, age, sex):
        if isinstance(name, str):
            self.full_name = name
        else:
            raise TypeError("Name should be a str ")
        if isinstance(surname, str):
            self.full_name += f" {surname}"
        else:
            raise TypeError("Surname should be a str")
        if isinstance(age, int) and age > 0:
            self.age = age
        else:
            raise TypeError("Age must be an int and must be higher than 0")
        if sex == "male" or sex == "female":
            self.sex = sex
        else:
            self.sex = "other"
        self.__answer = "don't know what you suggest"

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, new_answer):
        if isinstance(new_answer, str):
            self.__answer = new_answer
        else:
            raise TypeError("Answer should be a str")

    def __str__(self):
        if self.sex == "male":
            return f"This is a boy - {self.full_name}, {self.age} years old"
        elif self.sex == "female":
            return f"This is a girl - {self.full_name}, {self.age} years old"
        else:
            return f"This is a non-binary person - {self.full_name}, {self.age} years old"

    def ask_for_a_sexing(self, asked_person):
        print(f"{asked_person.full_name}, do you want to have sex with me - {self.full_name}?")

    def get_an_answer_for_sexing(self, asked_person):
        if asked_person.__answer == "yes":
            self.sexing(asked_person)
        else:
            print(f"{asked_person.full_name} doesn't want to have sex with {self.full_name}")

    def sexing(self, other_person):
        if isinstance(other_person, Person) and hash(self) == hash(other_person):
            print(f"mmm, {self.full_name} likes to masturbate")
        elif isinstance(other_person, Person) and self.sex == other_person.sex and self.sex != "other":
            print(f"mmm, {self.full_name} and {other_person.full_name} like to play pranks in a homo style")
        elif isinstance(other_person, Person) and self.sex != other_person.sex \
                and self.sex != "other" and other_person.sex != "other":
            print(f"mmm, {self.full_name} and {other_person.full_name} like to play pranks in a hetero style")

    def ask_for_a_couple(self, asked_person):
        print(f"{asked_person.full_name}, do you want to be in a relationship with me - {self.full_name}?")

    def get_an_answer_for_couple(self, asked_person):
        if asked_person.__answer == "yes":
            self.make_a_couple(asked_person)
        else:
            print(f"{asked_person.full_name} doesn't want to be in a relationship with {self.full_name}")

    def make_a_couple(self, other_person):
        for couple in range(len(Person.couples)):
            if self.full_name in Person.couples[couple]:
                raise AttributeError(f"{self.full_name} is already in a couple {Person.couples[couple]}")
            if other_person.full_name in Person.couples[couple]:
                raise AttributeError(f"{other_person.full_name} is already in a couple {Person.couples[couple]}")
        if isinstance(self, Person) and isinstance(other_person, Person):
            Person.couples.append((self.full_name, other_person.full_name))
            print(f"Year! {other_person.full_name} and {self.full_name} are a couple now!")
        else:
            print("Only person could make a couple")


dasha = Person("Dasha", "Motorina", 23, "female")
misha = Person("Misha", "Sukhorukov", 24, "male")
vova = Person("Vova", "Smolin", 21, "male")
masha = Person("Masha", "Gorshkova", 23, "female")

misha.ask_for_a_sexing(vova)
vova.answer = "no"
misha.get_an_answer_for_sexing(vova)
misha.ask_for_a_couple(dasha)
dasha.answer = "yes"
misha.get_an_answer_for_couple(dasha)
print(Person.couples)
