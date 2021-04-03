import cmath
import math
from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return (b ** 2) - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        det = (b ** 2) - 4 * a * c
        return det if det > 0 else float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        det = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(det)

        return (
            (-b + root_disc) / (2 * a),
            (-b - root_disc) / (2 * a)
        )


if __name__ == '__main__':
    # test 1
    _strategy = OrdinaryDiscriminantStrategy()
    solver = QuadraticEquationSolver(_strategy)
    results = solver.solve(1, 10, 16)
    assert complex(-2, 0) == results[0]
    assert complex(-8, 0) == results[1]

    _strategy = RealDiscriminantStrategy()
    solver = QuadraticEquationSolver(_strategy)
    results = solver.solve(1, 10, 16)
    assert complex(-2, 0) == results[0]
    assert complex(-8, 0) == results[1]

    _strategy = OrdinaryDiscriminantStrategy()
    solver = QuadraticEquationSolver(_strategy)
    results = solver.solve(1, 4, 5)
    assert complex(-2, 1), results[0]
    assert complex(-2, -1), results[1]

    _strategy = RealDiscriminantStrategy()
    solver = QuadraticEquationSolver(_strategy)
    results = solver.solve(1, 4, 5)
    assert math.isnan(results[0].real) is True
    assert math.isnan(results[1].real) is True
    assert math.isnan(results[0].imag) is True
    assert math.isnan(results[1].imag) is True
