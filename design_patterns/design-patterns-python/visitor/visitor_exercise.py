# taken from https://tavianator.com/the-visitor-pattern-in-python/
import unittest
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
    key = (_qualname(type(self)), type(arg))
    if not key in _methods:
        raise Exception('Key %s not found' % key)
    method = _methods[key]
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

# ↑↑↑ LIBRARY CODE ↑↑↑

class Value:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(Value)
    def visit(self, value):
        self.buffer.append(str(value.value))

    @visitor(MultiplicationExpression)
    def visit(self, me):
        self.visit(me.left)
        self.buffer.append('*')
        self.visit(me.right)

    @visitor(AdditionExpression)
    def visit(self, ae):
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append('+')
        self.visit(ae.right)
        self.buffer.append(')')

    def __str__(self):
        return "".join(self.buffer)


if __name__ == '__main__':
    _exp = AdditionExpression(
        Value(2), Value(3)
    )
    ep = ExpressionPrinter()
    ep.visit(_exp)
    print(ep)
    assert str(ep) == "(2+3)"

    expr = MultiplicationExpression(
        AdditionExpression(Value(2), Value(3)),
        Value(4)
    )
    ep1 = ExpressionPrinter()
    ep1.visit(expr)
    print(ep1)
    assert "(2+3)*4" == str(ep1)