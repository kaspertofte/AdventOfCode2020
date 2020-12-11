import unittest
from Day11.day11 import *


class Day11Test(unittest.TestCase):
    def test_single_move_part1(self):
        layout = SeatLayout.from_filename('day11.test')
        layout, changed = part1_move(layout)
        self.assertEqual("""#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""", layout.get_data())

    def test_challenge1_on_test_data(self):
        self.assertEqual(37, challenge1('day11.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(2296, challenge1('day11.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(26, challenge2('day11.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(2089, challenge2('day11.input'))


if __name__ == '__main__':
    unittest.main()
