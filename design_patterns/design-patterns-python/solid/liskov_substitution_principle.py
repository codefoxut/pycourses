# LSP
"""
The Liskov Substitution Principle states that subtypes should be substitutable for their base types.
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'

    @property
    def area(self):
        return self._height * self._width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


def use_it(obj):
    w = obj.width
    obj.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {obj.area}')


# creating a separate class was the wrong idea here.
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    use_it(sq)
