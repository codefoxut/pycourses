from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name}, ' \
               f'{len(self.inputs)} inputs, ' \
               f'{len(self.outputs)}.'

    def __iter__(self):
        yield self

    # def connect_to(self, other):
    #     self.outputs.append(other)
    #     other.inputs.append(self)


class NeuronLayer(list, Connectable):

    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(count):
            self.append(Neuron(f'{self.name}-{x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'


# def connect_to(self, other):
#     if self == other:
#         return
#
#     for s in self:
#         for o in other:
#             s.outputs.append(o)
#             o.inputs.append(s)


if __name__ == '__main__':
    n1 = Neuron('n1')
    n2 = Neuron('n2')
    l1 = NeuronLayer('L1', 5)
    l2 = NeuronLayer('L2', 3)

    # Neuron.connect_to = connect_to
    # NeuronLayer.connect_to = connect_to

    n1.connect_to(n2)
    n1.connect_to(l1)
    l1.connect_to(n2)
    l1.connect_to(l2)

    print(n1)
    print(n2)
    print(l1)
    print(l2)