import unittest
from Day14.day14 import *


class Day14Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(165, challenge1('day14.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(12512013221615, challenge1('day14.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(208, challenge2('day14_part2.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(3905642473893, challenge2('day14.input'))


if __name__ == '__main__':
    unittest.main()
