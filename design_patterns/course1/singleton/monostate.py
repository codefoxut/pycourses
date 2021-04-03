
class CEO:
    __shared_state = {
        'name': 'Adam',
        'age': 30
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 77
    print(ceo1, '\n', ceo2)

    cfo1 = CFO()
    cfo1.name = 'Shera'
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Raju'
    cfo2.money_managed = 10

    print(cfo1, '\n', cfo2)


