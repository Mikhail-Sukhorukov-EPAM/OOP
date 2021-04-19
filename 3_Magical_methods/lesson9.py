""" 3.9 Методы __getitem__ , __setitem__ и __delitem__
индексирование для экземпляров
"""


class SomeDict:
    def __init__(self, **kwargs):
        self.dict = dict(kwargs)

    def __str__(self):
        return str(self.dict)

    def __getitem__(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            raise KeyError("There is no a such key")

    def __setitem__(self, key, value):
        if key in self.dict.keys():
            print(f"Key '{key}' was rewritten with '{value}' value")
        else:
            print(f"Key '{key}' was added to dict with '{value}' value")
        self.dict[key] = value

    def __delitem__(self, key):
        if key in self.dict.keys():
            del self.dict[key]
        else:
            raise KeyError("There is no a such key")

"""
settings = {"name": "Mikhail", "surname": "Sukhorukov", "age": 24}
sd1 = SomeDict(**settings)
print(sd1["name"], sd1["surname"], sd1["age"])
sd1["job"] = "Software Test Automation Engineer"
print(sd1["job"])
sd1["age"] = 25
del sd1["job"]
print(sd1)
del sd1["agee"]
"""