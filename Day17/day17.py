class Board:
    neighbors = {}
    active_fields = set()
    N = 0

    def __init__(self, active_fields, N):
        self.active_fields = active_fields.copy()
        self.N = N

    @classmethod
    def from_file(cls, file_path, N):
        with open(file_path, "r") as file:
            data = file.read().strip().split("\n")

        active_fields = set()
        for x, line in enumerate(data):
            for y, c in enumerate(line):
                if c == '#':
                    cube = [x, y]
                    cube.extend([0]*(N-2))
                    active_fields.add(tuple(cube))
        return cls(active_fields, N)

    def is_active(self, coord):
        return coord in self.active_fields

    def get_neighbors(self, coord):
        if coord not in self.neighbors:
            neighbors = set()
            self.__recurse_get_neighbors(coord, neighbors, self.N)
            neighbors.remove(coord)
            self.neighbors[coord] = neighbors
        return self.neighbors[coord]

    def __recurse_get_neighbors(self, coord, neighbors, N):
        if N == 0:
            neighbors.add(coord)
            return neighbors
        for item in range(coord[N-1] - 1, coord[N-1] + 2):
            new_coord = list(coord)
            new_coord[N-1] = item
            self.__recurse_get_neighbors(tuple(new_coord), neighbors, N-1)
        return neighbors


def solve(board, N):
    for i in range(6):
        new_board = Board(set(), N)
        new_board.neighbors = board.neighbors
        all_neighbors = set()
        for cube in board.active_fields:
            neighbors = board.get_neighbors(cube)
            active_neighbors = {c for c in neighbors if board.is_active(c)}
            if len(active_neighbors) == 2 or len(active_neighbors) == 3:
                new_board.active_fields.add(cube)
            all_neighbors = all_neighbors.union(neighbors)

        inactive_cubes = {c for c in all_neighbors if not board.is_active(c)}
        for cube in inactive_cubes:
            active_neighbors = {c for c in board.get_neighbors(cube) if board.is_active(c)}
            if len(active_neighbors) == 3:
                new_board.active_fields.add(cube)

        board = new_board

    return len(board.active_fields)


def challenge1(file_path):
    board = Board.from_file(file_path, 3)
    return solve(board, 3)


def challenge2(file_path):
    board = Board.from_file(file_path, 4)
    return solve(board, 4)
