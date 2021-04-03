from abc import ABC


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


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


class SubtractionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} - {self.right}'


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, de: DoubleExpression):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        self.buffer.append('(')
        # ae.left.accept(self)
        self.visit(ae.left)
        self.buffer.append('+')
        # ae.right.accept(self)
        self.visit(ae.right)
        self.buffer.append(')')

    @visitor(SubtractionExpression)
    def visit(self, ae: SubtractionExpression):
        self.buffer.append('(')
        # ae.left.accept(self)
        self.visit(ae.left)
        self.buffer.append('-')
        # ae.right.accept(self)
        self.visit(ae.right)
        self.buffer.append(')')

    def __str__(self):
        return ''.join(self.buffer)


class ExpressionEvaluator:
    def __init__(self):
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, de):
        self.value = de.value

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.visit(ae.left)
        temp = self.value
        self.visit(ae.right)
        self.value += temp

    @visitor(SubtractionExpression)
    def visit(self, se):
        self.visit(se.left)
        temp = self.value
        self.visit(se.right)
        self.value = temp - self.value


if __name__ == '__main__':
    # 1 + (2 + 3)
    _exp = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    printer = ExpressionPrinter()
    printer.visit(_exp)
    print(printer)
    _exp2 = AdditionExpression(
        DoubleExpression(1),
        SubtractionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    printer = ExpressionPrinter()
    printer.visit(_exp2)
    print(printer)

    evaluator1 = ExpressionEvaluator()
    evaluator1.visit(_exp)
    print(evaluator1.value)
    evaluator1.visit(_exp2)
    print(evaluator1.value)