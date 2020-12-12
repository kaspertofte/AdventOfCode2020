class Ship:
    direction = []
    position = []

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __str__(self):
        return str(self.direction) + ' ' + str(self.position)


directions = {
    'N': (-1, 0),
    'E': (0, 1),
    'S':  (1, 0),
    'W': (0, -1)
}


def handle_instructions(ship, instruction, argument, instruction_operation):
    if instruction in directions:
        instruction_operation(ship, directions[instruction], argument)
    elif instruction == 'F':
        move(ship.position, ship.direction, argument)
    elif instruction == 'R':
        for i in range(argument // 90):
            ship.direction = [ship.direction[1], -ship.direction[0]]
    else:
        for i in range(argument // 90):
            ship.direction = [-ship.direction[1], ship.direction[0]]


def move(vector, direction, argument):
    vector[0] = vector[0] + direction[0] * argument
    vector[1] = vector[1] + direction[1] * argument


def move_direction(ship, direction, argument):
    move(ship.direction, direction, argument)


def move_position(ship, direction, argument):
    move(ship.position, direction, argument)


def challenge1(file_path):
    return read_data_and_handle_instructions(file_path, [0, 1], move_position)


def challenge2(file_path):
    return read_data_and_handle_instructions(file_path, [-1,10], move_direction)


def read_data_and_handle_instructions(file_path, initial_direction, instruction_operation):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    ship = Ship([0, 0], initial_direction)
    for d in data:
        handle_instructions(ship, d[0], int(d[1:]), instruction_operation)

    return abs(ship.position[0]) + abs(ship.position[1])