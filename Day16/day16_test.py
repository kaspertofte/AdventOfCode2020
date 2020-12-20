import unittest
from Day16.day16 import *


class Day16Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(71, challenge1('day16.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(25895, challenge1('day16.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(0, challenge2('day16.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(0, challenge2('day16.input'))


if __name__ == '__main__':
    unittest.main()
