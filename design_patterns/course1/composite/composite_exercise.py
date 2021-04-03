from abc import ABC
from collections.abc import Iterable
from unittest import TestCase


class FindSum(Iterable, ABC):
    @property
    def sum(self):
        _sum = 0
        for a in self:
            if isinstance(a, Iterable):
                for elem in a:
                    _sum += elem
            else:
                _sum += a
        return _sum


class SingleValue(FindSum):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, FindSum):
    pass


class Evaluate(TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)


if __name__ == '__main__':
    s1 = SingleValue(5)
    s2 = SingleValue(20)
    m1 = ManyValues()
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    m1.append(s1)
    m1.append(s2)
    m1.append(100)
    m1.append(other_values)
    print(m1.sum)