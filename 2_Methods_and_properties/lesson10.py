""" 2.6 Геттеры и сеттеры, property атрибуты """


"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Тип данных должен быть int или float")
        self.__balance = value

    def delete_balance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)


a = BankAccount("Mikhail", 100000)
a.balance
a.balance = 600
a.balance
del a.balance
"""


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str) and len(new_email.split("@")) == 2 and "." in new_email.split("@")[1]:
            self.__email = new_email
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3]  # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)
k.email = 'pppp@sdfsfsdfsdf'  # Ошибочная почта
print(k.email)
k.email = 'hello@re.w3'
print(k.email)