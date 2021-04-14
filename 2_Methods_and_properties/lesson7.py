"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sounds):
        return f"{self.name} says {sounds}"
"""


class Stack:
    def __init__(self):
        self.values = []

    def push(self, stack_item):
        self.values.append(stack_item)

    def is_empty(self):
        return True if len(self.values) == 0 else False

    def size(self):
        return len(self.values)

    def peek(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        return self.values[len(self.values)-1]

    def pop(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        return self.values.pop()


