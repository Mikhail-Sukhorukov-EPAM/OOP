""" 2.4 Моносостояние для экземпляров класса """


class Cat:
    __shared_attr = {
        "breed": "pers",
        "color": "black"
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr