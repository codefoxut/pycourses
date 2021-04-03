

def binary_search(container, item, left, right):
    # closing condition
    if left > right:
        return -1

    if container[left] == item:
        return left

    if container[right] == item:
        return right

    middle_index = (left + right) // 2
    if container[middle_index] == item:
        return middle_index
    elif container[middle_index] < item:
        print("checking item in right half...")
        return binary_search(container, item, middle_index + 1, right - 1)
    else:
        print("checking item in left half...")
        return binary_search(container, item, left + 1, middle_index - 1)


if __name__ == '__main__':
    lst = [1, 2, 3, 6, 8, 9, 11, 15, 16, 17, 19, 23, 34, 53, 76, 89, 93, 101, 121, 123, 178]
    print(f"item 15 found  at index", binary_search(lst, 15, 0, len(lst) - 1))
    print(f"item 45 found  at index", binary_search(lst, 45, 0, len(lst) - 1))
