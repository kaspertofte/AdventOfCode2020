import unittest
from Day6.day6 import *


class Day6Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(11, challenge1('day6.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(6885, challenge1('day6.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(6, challenge2('day6.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(3550, challenge2('day6.input'))


if __name__ == '__main__':
    unittest.main()
