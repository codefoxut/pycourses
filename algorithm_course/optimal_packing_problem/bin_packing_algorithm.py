

def first_fit_decreasing_algorithm(capactities, bin_max_capacity):
    # bin storage
    sol_bins = []

    item_list = list(capactities.items())
    print(item_list)

    sorted_items = sorted(item_list, key=lambda k: k[1], reverse=True)
    print(sorted_items)

    for item, val in sorted_items:
        bin_found = False

        for bins in sol_bins:
            total_bin_capacity = sum(capactities[i] for i in bins)
            remaining_capacity = bin_max_capacity - total_bin_capacity

            if remaining_capacity >= val:
                bins.append(item)
                bin_found = True
                break
        if not bin_found:
            sol_bins.append([item])

    print(sol_bins)



if __name__ == '__main__':
    cap = {'item1': 4,'item2': 2, 'item3': 6, 'item4': 5, 'item5': 3, 'item6': 7}
    first_fit_decreasing_algorithm(cap, 8)
