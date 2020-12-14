import itertools
import re

class Mask:
    zeros_mask = None
    ones_mask = None

    def __init__(self, zeros_mask, ones_mask):
        self.zeros_mask = zeros_mask
        self.ones_mask = ones_mask

    def apply(self, val):
        return (val | self.ones_mask) & self.zeros_mask

    def __str__(self):
        return '\nones_mask: ' + format(self.ones_mask, '036b') + '\nzero_mask: ' + format(self.zeros_mask, '036b') + '\n'


class MaskWithFloating:
    floating = []
    ones_mask = None

    def __init__(self, ones_mask, floating):
        self.floating = floating
        self.ones_mask = ones_mask

    def apply(self, val):
        return [f.apply(val | self.ones_mask) for f in self.floating]

    def __str__(self):
        return '\nones_mask: ' + format(self.ones_mask, '036b') + '\nfloating: ' + str(self.floating) + '\n'


def create_mask(line):
    zeros_mask = pow(2, 36)-1
    ones_mask = 0
    for i, val in enumerate(line):
        if val == '1':
            ones_mask = ones_mask | (1 << (35-i))
        if val == '0':
            zeros_mask = zeros_mask & ~(1 << (35-i))

    return Mask(zeros_mask, ones_mask)


def create_mask_part2(line):
    floating = []
    ones_mask = 0
    for i, val in enumerate(line):
        if val == '1':
            ones_mask = ones_mask | (1 << (35-i))
        if val == 'X':
            floating.append(i)

    floating_masks = []
    for c in itertools.product([0, 1], repeat=len(floating)):
        f_zeros_mask = pow(2, 36) - 1
        f_ones_mask = 0
        for i, f in enumerate(floating):
            if c[i] == 1:
                f_ones_mask = f_ones_mask | (1 << (35 - f))
            else:
                f_zeros_mask = f_zeros_mask & ~(1 << (35 - f))
        floating_masks.append(Mask(f_zeros_mask, f_ones_mask))

    return MaskWithFloating(ones_mask, floating_masks)


def challenge1(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    pattern = re.compile('mem\[(.{1,12})\]')
    mask = None
    result = {}
    for line in data:
        if line[0:4] == 'mask':
            mask = create_mask(line[7:])
        else:
            addr = int(pattern.match(line).group(1))
            val = int(line[line.find('=')+1:])
            result[addr] = mask.apply(val)

    return sum(result.values())


def challenge2(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n")

    pattern = re.compile('mem\[(.{1,12})\]')
    mask = None
    result = {}
    for line in data:
        if line[0:4] == 'mask':
            mask = create_mask_part2(line[7:])
        else:
            addr = int(pattern.match(line).group(1))
            val = int(line[line.find('=')+1:])
            for masked_address in mask.apply(addr):
                result[masked_address] = val

    return sum(result.values())
