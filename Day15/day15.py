def challenge1(file_path):
    return solve(file_path, 2020)


def challenge2(file_path):
    return solve(file_path, 30000000)


def solve(file_path,turns ):
    with open(file_path, "r") as file:
        data = file.read().strip().split(',')

    numbers_spoken = {int(number): idx+1 for idx, number in enumerate(data)}
    next_turn = len(data)+1
    next_number = 0
    while next_turn < turns:
        temp = next_number
        next_number = next_turn - numbers_spoken[next_number] if next_number in numbers_spoken else 0
        numbers_spoken[temp] = next_turn
        next_turn += 1

    return next_number
