
# circle square
# vector raster

# VectorCircle
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels a circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # super().draw()
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        super().resize(factor)


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    c1 = Circle(raster, 5)
    c1.draw()
    c1.resize(2)
    c1.draw()

    c2 = Circle(vector, 5)
    c2.draw()
    c2.resize(2)
    c2.draw()
