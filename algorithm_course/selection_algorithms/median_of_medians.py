
def median_algorithm(nums, k):
    # split into chunks of 5.
    chunks = [nums[i:i+5] for i in range(0, len(nums), 5)]
    print(chunks)

    # median
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]
    print("medians", medians)
    pivot_value = sorted(medians)[len(medians) // 2]

    # partitions
    left_array = [n for n in nums if n < pivot_value]
    right_array = [m for m in nums if m > pivot_value]
    print("left", left_array, "right", right_array)

    #selection phase
    pivot_index = len(left_array)

    if k < pivot_index:
        return median_algorithm(left_array, k)
    elif k > pivot_index:
        return median_algorithm(right_array, k - pivot_index - 1)
    else:
        return pivot_value


def select(nums, k):
    return median_algorithm(nums, k - 1)


if __name__ == '__main__':
    x = [1, 45, 23, 89, 10, 29, 32, 98, 34, 87,  67, 92, 77, 43, 29, 91, 39, 29, 99, 83, 85]
    print(select(x, 6))