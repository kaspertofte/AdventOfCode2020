import unittest
from Day5.day5 import *


class Day5Test(unittest.TestCase):

    def test_get_seat_id_on_FBFBBFFRLR(self):
        self.assertEqual(357, get_seat_id('FBFBBFFRLR'))

    def test_get_seat_id_on_BFFFBBFRRR(self):
        self.assertEqual(567, get_seat_id('BFFFBBFRRR'))

    def test_get_seat_id_on_FFFBBBFRRR(self):
        self.assertEqual(119, get_seat_id('FFFBBBFRRR'))

    def test_get_seat_id_on_BBFFBBFRLL(self):
        self.assertEqual(820, get_seat_id('BBFFBBFRLL'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(965, challenge1('day5.input'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(524, challenge2('day5.input'))


if __name__ == '__main__':
    unittest.main()
