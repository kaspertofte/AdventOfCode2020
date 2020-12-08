def get_upper_half(seat_range):
    range_length = int((seat_range.stop - seat_range.start+1)/2)-1
    return range(seat_range.stop - range_length, seat_range.stop)


def get_lower_half(seat_range):
    range_length = int((seat_range.stop - seat_range.start+1)/2)-1
    return range(seat_range.start, seat_range.start+range_length)


def get_seat_id(code):
    row_range = range(0, 127)
    col_range = range(0, 7)
    for c in code[0:7]:
        if c == 'F':
            row_range = get_lower_half(row_range)
        if c == 'B':
            row_range = get_upper_half(row_range)
    for c in code[7:10]:
        if c == 'L':
            col_range = get_lower_half(col_range)
        if c == 'R':
            col_range = get_upper_half(col_range)

    return row_range.start*8 + col_range.start


def challenge1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    max_seat_id = 0
    for line in data:
        seat_id = get_seat_id(line)
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


def challenge2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")
    seat_ids = list(map(get_seat_id, data))

    result = -1
    for s in range(0, 965):
        if s not in list(seat_ids):
            if (s+1) in list(seat_ids) and (s-1) in list(seat_ids):
                result = s
    return result
