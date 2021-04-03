"""
* designed by Tony Hoare.
* best case - O(N)
* worst case - O(N^2)
* in-place approach
"""
import random


class QuickSelect:

    def __init__(self, container):
        self.container = container
        self.first_index = 0
        self.last_index = len(container) - 1

    def run(self, k):
        return self.select(self.first_index, self.last_index, k - 1)

    def swap(self, i, j):
        self.container[i], self.container[j] = self.container[j], self.container[i]

    def select(self, first_index, last_index, k):

        pivot_index = self.partition(first_index, last_index)

        if pivot_index < k:
            return self.select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            return self.select(first_index, pivot_index -1, k)
        else:
            return self.container[pivot_index]

    def partition(self, first_index, last_index):
        pivot_index = random.randint(first_index, last_index)
        print("pivot=", pivot_index, first_index, last_index)

        self.swap(pivot_index, last_index)

        for i in range(first_index, last_index):
            if self.container[i] > self.container[last_index]:
                self.swap(i, first_index)
                first_index += 1
        print(self.container)
        self.swap(first_index, last_index)
        return first_index

    def sort(self):
        """sort after select element one by one."""
        sorted_list = []
        for i in range(1, len(self.container) + 1):
            sorted_list.append(self.run(i))
        return sorted_list


def quickselect(container, k_, index_first, index_last):
    pivot = partition(container, index_first, index_last)

    if pivot > k_:
        return quickselect(container, k_, index_first, pivot - 1)
    elif pivot < k_:
        return quickselect(container, k_, pivot + 1, index_last)
    else:
        return container[pivot]


def partition(container, index_first, index_last):
    pivot = random.randint(index_first, index_last)
    print("pivot=", pivot, index_last, index_first)
    # swap index_last with pivot
    container[index_last], container[pivot] = container[pivot], container[index_last]

    for i in range(index_first, index_last):
        if container[i] > container[index_last]:
            container[i], container[index_first] = container[index_first], container[i]
            index_first += 1

    container[index_last], container[index_first] = container[index_first], container[index_last]
    print("container", container)
    return index_first


if __name__ == '__main__':
    lst = [100, 54, 19, 39, 29, 84, 128, 234, 43, 20, 17, 92, 76, 25]
    l = 6
    q = QuickSelect(lst)
    # print(q.run(l))
    print(q.sort())
    print(quickselect(lst, l - 1, 0, len(lst) - 1))