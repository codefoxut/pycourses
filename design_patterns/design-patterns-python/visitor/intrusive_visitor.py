
class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} + {self.right}'

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == '__main__':
    # 1 + (2 + 3)
    exp = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    print(exp)
    buf = []
    exp.print(buf)
    print("".join(buf), ' = ', exp.eval())