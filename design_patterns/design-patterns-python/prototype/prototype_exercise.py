import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy1(self):
        # TODO
        return copy.deepcopy(self)

    def deep_copy(self):
        start1: Point = Point(self.start.x, self.start.y)
        end1: Point = Point(self.end.x, self.end.y)
        return Line(start=start1, end=end1)


if __name__ == '__main__':
    pass