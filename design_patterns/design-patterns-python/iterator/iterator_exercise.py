

class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent1 = self
        if right:
            self.right.parent1 = self

    def traverse_preorder1(self):
        for i in PreOrderIterator1(self):
            yield i.value

    def traverse_preorder(self):
        yield self.value
        if self.left:
            yield from self.left.traverse_preorder()
        if self.right:
            yield from self.right.traverse_preorder()

    def __repr__(self):
        return f'{self.value}'


class PreOrderIterator1:
    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current
        if self.current.left:
            self.current = self.current.left
            return self.current
        elif self.current.right:
            self.current = self.current.right
            return self.current
        elif self.current.parent1:
            p = self.current.parent1
            while p:
                if p.right and p.right != self.current:
                    self.current = p.right
                    return self.current
                else:
                    self.current = p
                    p = self.current.parent1
            else:
                raise StopIteration


if __name__ == '__main__':
    _root = Node(1, Node(2, Node(4, None, Node(8)), Node(5, Node(9), None)), Node(3, Node(6, None, Node(10)), Node(7, Node(11), None)))
    print(list(_root.traverse_preorder()))

    node = Node('a',
                Node('b',
                     Node('c'),
                     Node('d')),
                Node('e'))

    print("".join([x for x in node.traverse_preorder1()]))
