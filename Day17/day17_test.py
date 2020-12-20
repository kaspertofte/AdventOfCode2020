import unittest
from Day17.day17 import *


class Day17Test(unittest.TestCase):

    def test_challenge1_on_test_data(self):
        self.assertEqual(112, challenge1('day17.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(230, challenge1('day17.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(848, challenge2('day17.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(1600, challenge2('day17.input'))


if __name__ == '__main__':
    unittest.main()
