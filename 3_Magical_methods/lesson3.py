"""3.3 Магические методы __add__, __mul__, __sub__ и __truediv__"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        elif isinstance(other, BankAccount):
            return BankAccount(self.name, self.balance + other.balance)
        raise NotImplementedError("Implemented for int, float, BankAccount types")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.balance * other
        elif isinstance(other, BankAccount):
            return self.balance * other.balance
        raise NotImplementedError("Implemented for int, float, BankAccount types")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.balance - other
        elif isinstance(other, BankAccount):
            return self.balance - other.balance
        raise NotImplementedError("Implemented for int, float, BankAccount types")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.balance / other
        elif isinstance(other, BankAccount):
            return self.balance / other.balance
        raise NotImplementedError("Implemented for int, float, BankAccount types")

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        return self - other

    def __rtruediv__(self, other):
        return self / other

    def __repr__(self):
        return f"User: {self.name}, balance: {self.balance}"


b1 = BankAccount("M", 600)
b2 = BankAccount("D", 1000)

"""
print(b1 + 1)
print(b1 + b2)
print(2 + b1)
print(b1 + "[]")

print(b1 * 3)
print(3 * b1)
print(b1 * b2)

print(b1 - 30)
print(b1 - b2)
print(2 - b1)

print(b1 / 3)
print(b1 / b2)
print(3 / b1)
"""
