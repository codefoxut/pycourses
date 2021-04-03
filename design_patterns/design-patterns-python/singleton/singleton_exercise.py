
from design.course1.singleton.singleton_metaclass import Singleton


class Factory1:
    pass


class Factory2(metaclass=Singleton):
    pass


def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    a = factory()
    b = factory()
    return id(a) == id(b)


if __name__ == '__main__':
    print("Factory1 is singleton:", is_singleton(Factory1))
    print("Factory2 is singleton:", is_singleton(Factory2))