""" 2.11 Практика по методам и свойствам (property) """

from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = "you are an asshole"

    @property
    def secret(self):
        password = input("Input your password, please: ")
        if password == self.password:
            return self.__secret
        else:
            raise ValueError("Forbidden")

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_it_common_password(password):
        with open("passwords.txt") as common_passwords:
            for line in common_passwords:
                if line == password:
                    return True
            return False

    @password.setter
    def password(self, new_password):
        if isinstance(new_password, int):
            raise ValueError("A password must countain at least one letter")
        if not isinstance(new_password, str):
            raise TypeError("A password must be a string")
        if len(new_password) < 4:
            raise ValueError("A password must be higher than 4 symbols")
        if len(new_password) > 12:
            raise ValueError("A password must be less than 13 symbols")
        if not User.is_include_number(new_password):
            raise ValueError("A password must contain at least one digit")
        if not User.is_it_common_password(new_password):
            raise ValueError("A password must not be very simple")
        self.__password = new_password


u1 = User("Mikhail", "1111")
