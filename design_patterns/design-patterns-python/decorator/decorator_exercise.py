class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return 'A circle of radius %s' % self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return 'A square with side %s' % self.side


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        func = getattr(self.shape, 'resize', None)
        if callable(func):
            self.shape.resize(factor)

        # note that a Square doesn't have resize()

    def __str__(self):
        return '%s has the color %s' % (self.shape, self.color)


if __name__ == '__main__':
    circle = ColoredShape(Circle(2), 'red')
    print(circle)

    circle.resize(5)
    print(circle)

    sq = ColoredShape(Square(2), 'red')
    print(sq)

    sq.resize(5)
    print(sq)
