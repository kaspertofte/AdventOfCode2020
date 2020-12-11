class SeatLayout:
    def __init__(self, num_rows, num_cols, data):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = data

    @classmethod
    def from_filename(cls, file_path):
        with open(file_path, "r") as file:
            data = file.read().strip()

        num_rows = data.count('\n') + 1
        num_cols = data.find('\n')
        data = [c for c in data.replace('\n', '')]
        return cls(num_rows, num_cols, data)

    def copy(self):
        return SeatLayout(self.num_rows, self.num_cols, self.data.copy())

    def get_data(self):
        result = ''
        for r in range(0, self.num_rows):
            for c in range(0, self.num_cols):
                result += self.data[self.get_index(r, c)]
            result += '\n'
        return result

    def size(self):
        return len(self.data)

    def set(self, index, char):
        self.data[index] = char

    def get_adjacent_seats(self, index):
        result = []
        col = index % self.num_cols
        row = index // self.num_cols

        if col > 0:
            result.append(self.get_index(row, col - 1))
        if row > 0 and col > 0:
            result.append(self.get_index(row - 1, col - 1))
        if row > 0:
            result.append(self.get_index(row - 1, col))

        if row < self.num_rows - 1:
            result.append(self.get_index(row + 1, col))
        if col < self.num_cols - 1:
            result.append(self.get_index(row, col + 1))
        if (row < self.num_rows - 1) and (col < self.num_cols - 1):
            result.append(self.get_index(row + 1, col + 1))

        if (row > 0) and (col < self.num_cols - 1):
            result.append(self.get_index(row - 1, col + 1))
        if (row < self.num_rows - 1) and (col > 0):
            result.append(self.get_index(row + 1, col - 1))

        return result

    def get_visible_occupied_seats(self, index):
        result = []
        col = index % self.num_cols
        row = index // self.num_cols
        for i in range(min(self.num_cols - col - 1, row)):
            ne_index = self.get_index(row - i - 1, col + i + 1)
            if self.data[ne_index] == '#':
                result.append(ne_index)
                break
            if self.data[ne_index] == 'L':
                break

        for i in range(min(col, self.num_rows - row - 1)):
            sw_index = self.get_index(row + i + 1, col - i - 1)
            if self.data[sw_index] == '#':
                result.append(sw_index)
                break
            if self.data[sw_index] == 'L':
                break

        for i in range(min(self.num_cols - col - 1, self.num_rows - row - 1)):
            se_index = self.get_index(row + i + 1, col + i + 1)
            if self.data[se_index] == '#':
                result.append(se_index)
                break
            if self.data[se_index] == 'L':
                break

        for c in range(col+1, self.num_cols):
            e_index = self.get_index(row, c)
            if self.data[e_index] == '#':
                result.append(e_index)
                break
            if self.data[e_index] == 'L':
                break

        for r in range(row+1, self.num_rows):
            s_index = self.get_index(r, col)
            if self.data[s_index] == '#':
                result.append(s_index)
                break
            if self.data[s_index] == 'L':
                break

        for i in range(min(col, row)):
            nw_index = self.get_index(row - i - 1, col - i - 1)
            if self.data[nw_index] == '#':
                result.append(nw_index)
                break
            if self.data[nw_index] == 'L':
                break

        for c in reversed(range(col)):
            w_index = self.get_index(row, c)
            if self.data[w_index] == '#':
                result.append(w_index)
                break
            if self.data[w_index] == 'L':
                break

        for r in reversed(range(row)):
            n_index = self.get_index(r, col)
            if self.data[n_index] == '#':
                result.append(n_index)
                break
            if self.data[n_index] == 'L':
                break

        return result

    def get_index(self, row, col):
        return col + row * self.num_cols

    def count_occupied(self, seats):
        result = 0
        for seat in seats:
            if self.data[seat] == '#':
                result += 1
        return result

    def count_free(self, seats):
        result = 0
        for seat in seats:
            if self.data[seat] != '#':
                result += 1
        return result

    def is_floor(self, index):
        return self.data[index] == '.'

    def is_occupied(self, index):
        return self.data[index] == '#'

    def is_free(self, index):
        return self.data[index] == 'L'

    def num_occupied(self):
        result = 0
        for s in self.data:
            if s == '#':
                result += 1
        return result


def move(old_layout, threshold, adjacency_rule):
    layout = old_layout.copy()
    changed = False
    for i in range(0,old_layout.size()):
        if old_layout.is_floor(i):
            continue

        seats = adjacency_rule(i)
        num_occupied = old_layout.count_occupied(seats)
        if old_layout.is_free(i) and num_occupied == 0:
            layout.set(i, '#')
            changed = True

        if old_layout.is_occupied(i) and num_occupied >= threshold:
            layout.set(i, 'L')
            changed = True

    return layout, changed


def challenge1(file_path):
    layout = SeatLayout.from_filename(file_path)
    changed = True
    while changed:
        layout, changed = move(layout, 4, layout.get_adjacent_seats)

    return layout.num_occupied()


def challenge2(file_path):
    layout = SeatLayout.from_filename(file_path)
    changed = True
    while changed:
        layout, changed = move(layout, 5, layout.get_visible_occupied_seats)

    return layout.num_occupied()
