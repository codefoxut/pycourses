import math
from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * math.sin(b)
            self.y = a * math.cos(b)


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.sin(theta), rho * math.cos(theta))


class Point:
    factory = PointFactory()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y:{self.y}'

    # factory method.
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.sin(theta), rho * math.cos(theta))


if __name__ == '__main__':
    p = Point(2, 3)
    print("p", p)

    p2 = Point.new_polar_point(4, math.asin(3/5))
    print("p2", p2)

    p3 = PointFactory.new_cartesian_point(3, 4)
    print("p3", p3)

    p4 = Point.factory.new_polar_point(3, math.pi/6)
    print("p4", p4)