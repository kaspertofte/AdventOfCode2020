import unittest
from Day18.day18 import *


class Day18Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        with open('day18.test', "r") as file:
            data = file.read().strip().split("\n")
        self.assertEqual(15, compute_part1('2 + 4 + 9'))
        self.assertEqual(54, compute_part1('2 + 4 * 9'))
        self.assertEqual(38, compute_part1('2 + (4 * 9)'))
        self.assertEqual(26, compute_part1(data[0]))
        self.assertEqual(437, compute_part1(data[1]))
        self.assertEqual(12240, compute_part1(data[2]))
        self.assertEqual(13632, compute_part1(data[3]))


    def test_challenge1_on_real_data(self):
        self.assertEqual(510009915468, challenge1('day18.input'))

    def test_challenge2_on_test_data(self):
        with open('day18.test', "r") as file:
            data = file.read().strip().split("\n")
        self.assertEqual(26, compute_part2('2 * 4 + 9'))
        self.assertEqual(15, compute_part2('2 + 4 + 9'))
        self.assertEqual(54, compute_part2('2 + 4 * 9'))
        self.assertEqual(38, compute_part2('2 + (4 * 9)'))
        self.assertEqual(46, compute_part2(data[0]))
        self.assertEqual(1445, compute_part2(data[1]))
        self.assertEqual(669060, compute_part2(data[2]))
        self.assertEqual(23340, compute_part2(data[3]))

    def test_challenge2_on_real_data(self):
        self.assertEqual(321176691637769, challenge2('day18.input'))


if __name__ == '__main__':
    unittest.main()
