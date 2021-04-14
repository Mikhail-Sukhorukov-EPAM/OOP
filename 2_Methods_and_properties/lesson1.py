"""2.1 Методы экземпляра. Аргумент self"""


class Counter:
    start_value = 0

    def start_from(self, value=0):
        self.start_value = value

    def increment(self):
        self.start_value += 1

    def display(self):
        print("Текущее значение счетчика = "+str(self.start_value)+"")

    def reset(self):
        self.start_value = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display()  # печатает "Текущее значение счетчика


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, next_point):
        if isinstance(next_point, Point):
            self.distance = ((next_point.x - self.x)**2 + (next_point.y - self.y)**2)**(0.5)
            return self.distance
        else:
            print("Передана не точка")


p1 = Point()
p2 = Point()
p2.set_coordinates(1, 2)
p1.set_coordinates(4, 6)
p1.get_distance(p2)

