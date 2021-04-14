"""
class Point:
    list_points = []
    def __init__(self, x=0, y=0):
        self.coordinate_list = []
        self.x = x
        self.y = y
        Point.list_points.append(self)

    def input_values(self):
        try:
            self.x = int(input("Input X: "))
            self.y = int(input("Input Y: "))
            self.coordinate_list.append(self.x)
            self.coordinate_list.append(self.y)
        except ValueError:
            print("Неправильный формат данных")

    def print_coordinates(self):
        print(self.coordinate_list)

    def return_coordinates(self):
        return self.coordinate_list


N = int(input("Запросите колличевство экземпляров: "))

all_coordinates = []
for i in range(N):
    i = Point()
    i.input_values()
    all_coordinates.append(i.return_coordinates())

print(all_coordinates)
"""


"""
class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.list_of_coordinates = [self.x, self.y, self.z]

    def change_one_coordinate(self, value, coordinate):
        " [0] - x, [1] - y, [2] - z, [coordinate] "
        self.list_of_coordinates[coordinate] = value

    def change_all_coordinate(self, x, y, z):
        self.list_of_coordinates = [x, y, z]

    def return_coordinates(self):
        return tuple(self.list_of_coordinates)
"""


"""
class Point:
    def __init__(self, another_example=0):
        if isinstance(another_example, Point):
            self.x = another_example.x
            self.y = another_example.y
            self.list_of_coordinates = [self.x, self.y]
        else:
            self.x = x
            self.y = y
            self.list_of_coordinates = [self.x, self.y]
"""
