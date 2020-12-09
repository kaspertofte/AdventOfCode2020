from queue import Queue


def challenge1(file_path, preamble_length):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    data = list(map(int, data))

    result = get_first_invalid_number(data, preamble_length)
    return result


def get_first_invalid_number(input, size):
    i = 0
    active_numbers = Queue(size)
    while i < size:
        active_numbers.put(input[i])
        i += 1

    while i < len(input):
        if not is_sum_present(list(active_numbers.queue), input[i]):
            return input[i]
        active_numbers.get()
        active_numbers.put(input[i])
        i += 1

    return -1


def is_sum_present(input, sum):
    for i in range(0, len(input)-1):
        for j in range(i+1, len(input)):
            if input[i] + input[j] == sum:
                return True
    return False


def challenge2(file_path, preamble_length):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    data = list(map(int, data))

    first_invalid_number = get_first_invalid_number(data, preamble_length)

    contiguous_set = get_contiguous_set_that_sums(data, first_invalid_number)
    return min(contiguous_set) + max(contiguous_set)


def get_contiguous_set_that_sums(input, target_sum):
    for i in range(0, len(input)-1):
        j = i + 1
        sum = input[i] + input[j]
        result = [input[i], input[j]]
        while sum <= target_sum:
            if sum == target_sum:
                return result
            j += 1
            sum += input[j]
            result.append(input[j])
    return []
