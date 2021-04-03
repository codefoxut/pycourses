import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p, q):
    """euclidean distance."""
    return math.sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)


def brute_force_approach(sub_array):
    # distance between all the  points of sub array.
    min_distance = float('inf')
    for i in range(len(sub_array) - 1):
        for j in range(i + 1, len(sub_array)):
            actual_distance = distance(sub_array[i], sub_array[j])
            if actual_distance < min_distance:
                min_distance = actual_distance
    return min_distance


def closest_pairs_problem(list_sorted_x, list_sorted_y, num_of_items):
    if num_of_items <= 3:
        return brute_force_approach(list_sorted_x)

    middle_index = num_of_items // 2
    middle_item = list_sorted_x[middle_index]

    # divide phase
    delta_left = closest_pairs_problem(list_sorted_x[:middle_index], list_sorted_y, middle_index)
    delta_right = closest_pairs_problem(list_sorted_x[middle_index:], list_sorted_y,
                                        num_of_items - middle_index)

    # conquer phase
    delta = min(delta_left, delta_right)
    strip_points = [k for k in list_sorted_y if abs(k.x - middle_item.x) < delta]
    strip_delta = get_strip_delta(strip_points, delta)
    return min(strip_delta, delta)


def get_strip_delta(strip_points, delta):
    min_distance = delta
    n = len(strip_points)

    for i in range(n):
        j = i + 1
        while j < n and abs(strip_points[i].y - strip_points[j].y) < min_distance:
            min_distance = distance(strip_points[i], strip_points[j])
            j += 1

    return min_distance


def run(point_list):
    x_list = sorted(point_list, key=lambda k: k.x)
    y_list = sorted(point_list, key=lambda k: k.y)
    return closest_pairs_problem(x_list, y_list, len(point_list))


if __name__ == '__main__':
    p_list = [Point(1, 1), Point(4, 2), Point(10, 10), Point(0, 0), Point(5, 3), Point(0, 1),]
    print(run(p_list))

