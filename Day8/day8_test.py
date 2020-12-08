import unittest
from Day8.day8 import *


class Day8Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(5, challenge1('day8.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(1801, challenge1('day8.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(8, challenge2('day8.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(2060, challenge2('day8.input'))


if __name__ == '__main__':
    unittest.main()
