""" 5.4 Инструкция raise
если raise AttributeError from None - только одна ошибка (AttributeError)
если raise AttributeError from second - все три ошибки
если raise AttributeError from first - две ошибки (TypeError, AttributeError)"""


try:
    raise TypeError
except TypeError as first:
    try:
        raise IndexError
    except IndexError as second:
        raise AttributeError from first

