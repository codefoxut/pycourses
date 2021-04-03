import random
import string


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class User2:
    strings = []

    def __init__(self, name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x)
                      for x in name.split(' ')]

    def __repr__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for _ in range(8)])


if __name__ == '__main__':
    users = []
    users2 = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))
            users2.append(User2(f'{first} {last}'))

    print(users)
    print(users2)