class ByteCode:
    def __init__(self, instruction, argument):
        self.instruction = instruction
        self.argument = argument


def read_bytecode(data):
    bytecodes = []
    for line in data:
        entries = line.split(' ')
        bytecodes.append(ByteCode(entries[0], int(entries[1])))
    return bytecodes


class LoopException(Exception):
    def __init__(self, id, accumulator):
        self.id = id
        self.accumulator = accumulator


def execute_program(bytecodes, bytecode_instructions):
    executed_bytecodes = []
    program_counter = 0
    accumulator = 0
    while program_counter < len(bytecodes):
        if program_counter in executed_bytecodes:
            raise LoopException(program_counter, accumulator)
        executed_bytecodes.append(program_counter)
        bytecode = bytecodes[program_counter]
        accumulator, program_counter = bytecode_instructions[bytecode.instruction](accumulator, program_counter, bytecode.argument)

    return accumulator


def nop_instruction(accumulator, program_counter, args):
    return accumulator, program_counter+1


def jmp_instruction(accumulator, program_counter, args):
    return accumulator, program_counter+args


def acc_instruction(accumulator, program_counter, args):
    return accumulator + args, program_counter+1


instructions = {
    'nop': nop_instruction,
    'jmp': jmp_instruction,
    'acc': acc_instruction
}


def challenge1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    program = read_bytecode(data)
    try:
        result = execute_program(program, instructions)
    except LoopException as e:
        result = e.accumulator

    return result


def execute_modified_program(program, bytecode, new_instruction):
    new_program = program.copy()
    idx = new_program.index(bytecode)
    new_program[idx] = ByteCode(new_instruction, bytecode.argument)
    return execute_program(new_program, instructions)


def challenge2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    program = read_bytecode(data)
    result = -1
    for bytecode in program:
        if bytecode.instruction == 'jmp':
            try:
                result = execute_modified_program(program, bytecode, 'nop')
                break
            except LoopException:
                pass
        elif bytecode.instruction == 'nop':
            try:
                result = execute_modified_program(program, bytecode, 'jmp')
                break
            except LoopException:
                pass

    return result
