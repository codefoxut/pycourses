"""
the Open-Closed Principle, which states that classes should be open for extension,
but closed for modification. In other words, you should extend functionality using
interfaces and inheritance rather than jumping back into already-written/tested
code and adding to it or changing it.
"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    @staticmethod
    def filter_by_color(products, color):
        for item in products:
            if item.color == color:
                yield item

    @staticmethod
    def filter_by_size(products, size):
        for item in products:
            if item.size == size:
                yield item

    @staticmethod
    def filter_by_size_and_color(products, size, color):
        for item in products:
            if item.size == size and item.color == color:
                yield item


# specification

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return any(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    product_list = [apple, tree, house]

    pf = ProductFilter()
    print(" Green products (old):")
    for p in pf.filter_by_color(product_list, Color.GREEN):
        print(f' - {p.name} is green.')

    bf = BetterFilter()
    print(" Green products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(product_list, green):
        print(f' - {p.name} is green')

    print("large products.")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(product_list, large):
        print(f' - {p.name} is large!')

    print("large blue products.")
    large_blue = AndSpecification(SizeSpecification(Size.LARGE), ColorSpecification(Color.BLUE))
    for p in bf.filter(product_list, large_blue):
        print(f' - {p.name} is large and blue.')

    print("small green products.")
    small_green = SizeSpecification(Size.SMALL) & ColorSpecification(Color.GREEN)
    for p in bf.filter(product_list, small_green):
        print(f' - {p.name} is small and green.')

    print("large green products.")
    large_or_green = SizeSpecification(Size.LARGE) | ColorSpecification(Color.GREEN)
    for p in bf.filter(product_list, large_or_green):
        print(f' - {p.name} is large or green.')
