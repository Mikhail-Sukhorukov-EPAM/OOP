"""3.7 Магический метод __call__
экземпляры класса нельзя вызвать ()
класс - можно"""
from time import perf_counter


class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.lenth = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.lenth += len(args)
        print(f"Наш объект вызывлся {self.counter} раз")

    def average(self):
        return self.summa / self.lenth


"""
c1 = Counter()
c1(7, 8)
print(c1.average())
c1(8, 9, 0)
print(c1.average())
"""


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция {self.func.__name__}")
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f"Функия отработала за {finish - start}")
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
    return pr


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


print(Timer(fib)(9))
