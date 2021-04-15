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


class Vector:
    def __init__(self, *args):
        self.values = sorted([arg for arg in args if isinstance(arg, int)])

    def __str__(self):
        if not self.values:
            return "Пустой вектор"
        else:
            return f"Вектор{(*sorted(self.values),)}"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[x + other for x in self.values])
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[sum(pair) for pair in zip(self.values, other.values)])
            else:
                print("Сложение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[x * other for x in self.values])
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[pair[0] * pair[1] for pair in zip(self.values, other.values)])
            else:
                print("Умножение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя умножать с {other}")

    def __rmul__(self, other):
        return self * other


v1 = Vector(1, 2, 3)
v2 = Vector(3, 2, 1)
v3 = Vector(4, 5, 6, 6)
"""
print(1 + v1)
print(3 * v1)
print(v1 + v2)
print(v2 + v1)
print(v1 * v2)
print(v2 * v1)
print(v1 * v3)
"""
