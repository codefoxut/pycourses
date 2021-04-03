
def merge_sort(nums, reverse=False):

    if len(nums) == 1:
        return

    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]
    merge_sort(left_half, reverse=reverse)
    merge_sort(right_half, reverse=reverse)
    cmp_func_str = '__gt__' if reverse else '__lt__'

    i, j, k = 0, 0, 0
    while i < len(left_half) and j < len(right_half):
        if getattr(left_half[i], cmp_func_str)(right_half[j]):
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        nums[k] = left_half[i]
        i, k = i + 1, k + 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j, k = j + 1, k + 1

    return nums


if __name__ == '__main__':
    lst = [1, 85, 19, 2, 49, 19, 47, 92, 85, 10, -2, -58, 29]
    merge_sort(lst, reverse=True)
    print(lst)

    my_list = [1, 5, -2, 0, 10, 100, 55, 12, 10, 2, -10, -3]

    merge_sort(my_list)
    print(my_list)
