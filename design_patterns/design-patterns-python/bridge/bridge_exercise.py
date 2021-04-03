import unittest
from abc import ABC


class Shape:
    def __init__(self, renderer, name):
        self.name = name
        self.renderer = renderer

    def __str__(self):
        return f'Drawing {self.name} {self.renderer.what_to_render_as}'


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')


class VectorSquare(Square):
    def __str__(self):
        return f'Drawing {self.name} as lines'


class RasterSquare(Square):
    def __str__(self):
        return f'Drawing {self.name} as pixels'


class VectorTriangle(Triangle):
    def __str__(self):
        return f'Drawing {self.name} as lines'


class RasterTriangle(Triangle):
    def __str__(self):
        return f'Drawing {self.name} as pixels'


class Renderer(ABC):
    shape = None

    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"


class Evaluate(unittest.TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), 'Drawing Square as lines')

    def test_pixel_triangle(self):
        tr = Triangle(RasterRenderer())
        self.assertEqual(str(tr), 'Drawing Triangle as pixels')


if __name__ == '__main__':
    print(str(Triangle(RasterRenderer())))