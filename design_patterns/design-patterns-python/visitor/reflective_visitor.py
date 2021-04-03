from abc import ABC


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} + {self.right}'


class ExpressionPrinter:
    @staticmethod
    def print(exp, buffer):
        if isinstance(exp, DoubleExpression):
            buffer.append(str(exp.value))
        elif isinstance(exp, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(exp.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(exp.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)


if __name__ == '__main__':
    # 1 + (2 + 3)
    _exp = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    print(_exp)
    buf = []
    buf1 = []
    _exp.print(buf1)
    ExpressionPrinter.print(_exp, buf)
    print("".join(buf1))
    print("".join(buf), ' = ', 'exp.eval()')