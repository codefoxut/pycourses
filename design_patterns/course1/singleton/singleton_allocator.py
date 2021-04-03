import random


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        _id = random.randint(1, 101)
        print(f'id = {_id}')
        print("Loading a database form file...")


if __name__  == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 is d2)
    print(id(d1), id(d2))