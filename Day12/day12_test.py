import unittest
from Day12.day12 import *


class Day12Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(25, challenge1('day12.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(1221, challenge1('day12.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(286, challenge2('day12.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(59435, challenge2('day12.input'))


if __name__ == '__main__':
    unittest.main()
