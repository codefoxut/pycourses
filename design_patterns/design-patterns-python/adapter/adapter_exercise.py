
class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


if __name__ == '__main__':
    sq = Square(11)
    adapter = SquareToRectangleAdapter(sq)
    print(calculate_area(adapter))
    sq.side = 10
    print(calculate_area(adapter))