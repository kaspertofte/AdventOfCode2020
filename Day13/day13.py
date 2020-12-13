import functools


def challenge1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    bus_ids_with_waiting_times = [(int(b), int(b) - int(data[0]) % int(b)) for i, b in enumerate(data[1].split(',')) if b != 'x']
    result = min(bus_ids_with_waiting_times, key=lambda bus: bus[1])

    return result[0] * result[1]


# this is a chinese_remainder problem since
# we want (x + i) = 0 (mod ID) where i is the index of the bus for each bus
# this is equivalent to x = -i (mod ID) for each bus
# the chinese remainder theorem only holds if all the divisors (n_i or ID in our case) are
# pairwise co-primes, but since they are all primes they are also pairwise co-primes
def challenge2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    bus_ids_with_mods = [(int(bus), -i % int(bus)) for i, bus in enumerate(data[1].split(',')) if bus != "x"]

    return chinese_remainder(bus_ids_with_mods)


# chinese remainder list of tuples with (divisor, remainder)
# solves the problem of finding an x such that:
# x = a_i (mod n_i) for i = 1..k
# we call a_i the remainder and n_i the divisor
def chinese_remainder(moduli):
    result = 0
    N = functools.reduce((lambda value, mod: value * mod[0]), moduli, 1)
    for mod in moduli:
        b = N // mod[0]
        result += mod[1] * b * pow(b, -1, mod[0])

    return result % N
