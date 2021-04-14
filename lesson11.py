""" 2.7 Декоратор Property property атрибуты """

"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Тип данных должен быть int или float")
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        del self.__balance


b1 = BankAccount("Mikhail", 1000000)
print(b1.my_balance)
b1.my_balance = 1000000001
print(b1.my_balance)
b1.my_balance = 1
print(b1.my_balance)
"""


class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollars):
        if isinstance(new_dollars, int) and new_dollars > 0:
            self.total_cents = self.total_cents % 100 + new_dollars * 100
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        if isinstance(new_cents, int) and 0 < new_cents < 100:
            self.total_cents = self.total_cents // 100 * 100 + new_cents
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


m1 = Money(100, 2)
print(m1)
print(m1.total_cents)
print(m1.dollars)
m1.dollars = 655
print(m1.dollars)
print(m1.total_cents)
print(m1.cents)
m1.cents = 45
print(m1.cents)
print(m1.total_cents)
print(m1)

Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)
