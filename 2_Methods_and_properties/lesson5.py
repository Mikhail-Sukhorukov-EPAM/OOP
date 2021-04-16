""" 2.5 Публичные, приватные, защищенные атрибуты и методы
Инкапсуляция - механизм языка, позволяющий объединить данные и методы, работающие с этими данными,
в единый объект и скрыть детали реализации от пользователя."""


class BankAccount:
    def __init__(self, name, balance, passport):
        """ self.name = name - публичный, self._balance = balance - защищенный (для разработчиков)
        , self.__passport = passport - приватный (невозможно извлечь вне класса) """
        self.name = name
        self._balance = balance
        self.__passport = passport

    def print_public_data(self):
        print(self.name)

    def print_protected_data(self):
        print(self._balance)

    def print_private_data(self):
        print(self.__passport)


account1 = BankAccount("Bob", 10000, 131231)
account1.print_public_data()
account1.print_protected_data()
account1.print_private_data()
print(account1.name)
print(account1._balance)
print(account1.__passport)
