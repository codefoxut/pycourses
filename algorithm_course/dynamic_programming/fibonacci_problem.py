

class FibonacciNumber:

    def __init__(self):
        self.memoization_table: dict = {0: 0, 1: 1}

    def naive_approach(self, n):

        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.naive_approach(n - 1) + self.naive_approach(n - 2)

    def fibonacci_memoize(self, n):
        if n in self.memoization_table:
            return self.memoization_table[n]

        result = self.fibonacci_memoize(n - 1) + self.fibonacci_memoize(n - 2)
        self.memoization_table[n] = result
        return result


if __name__ == '__main__':
    print(FibonacciNumber().naive_approach(100))
    print(FibonacciNumber().fibonacci_memoize(100))
