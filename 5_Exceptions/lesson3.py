""" 5.3 Обработка исключений try-except """


try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    "если нет никакого экспепшена"
finally:
    print("конец")
