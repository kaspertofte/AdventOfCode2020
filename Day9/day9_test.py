import unittest
from Day9.day9 import *


class Day9Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(127, challenge1('day9.test', 5))

    def test_challenge1_on_real_data(self):
        self.assertEqual(90433990, challenge1('day9.input', 25))

    def test_challenge2_on_test_data(self):
        self.assertEqual(62, challenge2('day9.test', 5))

    def test_challenge2_on_real_data(self):
        self.assertEqual(0, challenge2('day9.input', 25))


if __name__ == '__main__':
    unittest.main()
