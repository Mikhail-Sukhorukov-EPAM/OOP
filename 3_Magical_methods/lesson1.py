"""3.1 Магические методы. Методы __str__ и __repr__"""


class User:
    users = []

    def __init__(self, user):
        self.user = user
        User.users.append(self.user)

    def __str__(self):
        # u1
        # < __main__.User object at 0x1085271f0 >
        # print(u1)
        # It is a user: Mikhail
        # str(u1)
        # 'It is a user: Mikhail'
        return f"It is a user: {self.user}"

    def __repr__(self):
        # u1
        # It is a user: Mikhail
        # print(u1)
        # It is a user: Mikhail
        # str(u1)
        # 'It is a user: Mikhail'
        return f"User: {self.user}, List of Users: {User.users}"
