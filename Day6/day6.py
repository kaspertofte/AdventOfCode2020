def count_unique_chars(data):
    result = 0
    for i in range(97, 123):
        if data.find(chr(i)) > -1:
            result += 1
    return result


def count_chars_repeated_on_all_lines(data):
    lines = data.split("\n")

    result = 0
    for i in range(97, 123):
        num_occurrences = 0
        for line in lines:
            if line.find(chr(i)) > -1:
                num_occurrences += 1
        if num_occurrences == len(lines):
            result += 1

    return result


def challenge1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n\n")

    result = 0
    for line in data:
        result += count_unique_chars(line)

    return result


def challenge2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n\n")


    result = 0
    for line in data:
        result += count_chars_repeated_on_all_lines(line)

    return result
