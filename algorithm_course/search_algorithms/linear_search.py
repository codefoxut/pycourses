

def linear_search(container, item):

    for index in range(len(container)):
        if container[index] == item:
            return index

    return -1


def linear_search_recursion(container, item, index=0):

    if index == len(container):
        return -1

    if container[index] == item:
        return index

    return linear_search_recursion(container, item, index + 1)


if __name__ == '__main__':
    lst = [1, 2, 3, 6, 8, 9, 11, 15, 16, 17, 19, 23, 34, 53, 76, 89, 93]
    print(f"item 15 found  at index", linear_search(lst, 15))
    print(f"item 45 found  at index", linear_search(lst, 45))

    print(f"item 15 found  at index", linear_search_recursion(lst, 15))
    print(f"item 45 found  at index", linear_search_recursion(lst, 45))