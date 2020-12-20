def add(lhs, rhs):
    return lhs + rhs


def multiply(lhs, rhs):
    return lhs * rhs


class Expression:
    lhs = 0
    rhs = 0

    def __init__(self, lhs, rhs, operator):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = operator

    def evaluate(self):
        lv = self.lhs.evaluate() if type(self.lhs).__name__ == 'Expression' else self.lhs
        rv = self.rhs.evaluate() if type(self.rhs).__name__ == 'Expression' else self.rhs
        return self.operator(lv, rv)


def compute_part1(expression):
    stack = []
    active_expression = Expression(0, 0, add)
    operator = add
    for i, c in enumerate(expression):
        if c == ' ':
            continue
        if c == '(':
            stack.append((active_expression, operator))
            active_expression = Expression(0, 0, add)
            operator = add
        elif c == ')':
            state = stack.pop()
            active_expression = Expression(state[0], active_expression, state[1])
        elif c == '+':
            operator = add
        elif c == '*':
            operator = multiply
        else:
            active_expression = Expression(active_expression, int(c), operator)

    return active_expression.evaluate()


def challenge1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    return sum([compute_part1(exp) for exp in data])


def compute_part2(expression):
    stack = []
    active_expression = Expression(0, 0, add)
    factors = []
    operator = add
    for i, c in enumerate(expression):
        if c == ' ':
            continue
        if c == '(':
            stack.append((active_expression, operator, factors))
            active_expression = Expression(0, 0, add)
            factors = []
            operator = add
        elif c == ')':
            state = stack.pop()
            while len(factors) > 0:
                active_expression = Expression(active_expression, factors.pop(), multiply)
            active_expression = Expression(state[0], active_expression, state[1])
            operator = state[1]
            factors = state[2]
        elif c == '+':
            operator = add
        elif c == '*':
            operator = multiply
            factors.append(active_expression)
            active_expression = Expression(1, 0, add)
        else:
            active_expression = Expression(active_expression, int(c), operator)

    while len(factors) > 0:
        active_expression = Expression(active_expression, factors.pop(), multiply)

    return active_expression.evaluate()


def challenge2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    return sum([compute_part2(exp) for exp in data])

