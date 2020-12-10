def get_sorted_data(file_path):
    with open(file_path, "r") as file:
        data = list(map(int, file.read().strip().split("\n")))

    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    return data


def challenge1(file_path):
    data = get_sorted_data(file_path)
    num_ones = 0
    num_threes = 0
    for i in range(0, len(data)-1):
        if data[i+1] - data[i] == 1:
            num_ones += 1
        if data[i+1] - data[i] == 3:
            num_threes += 1

    return num_ones*num_threes


def challenge2(file_path):
    data = get_sorted_data(file_path)

    cache = {len(data) - 1: 1}

    return get_num_combinations_from_index(data, 0, cache)


def get_num_combinations_from_index(data, index, cache):
    if index in cache:
        return cache.get(index)

    num_paths = 0
    i = 1
    while (index + i) < len(data) and data[index + i] - data[index] < 4:
        num_paths += get_num_combinations_from_index(data, index + i, cache)
        i += 1

    cache[index] = num_paths
    return num_paths
