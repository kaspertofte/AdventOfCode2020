import unittest
from Day10.day10 import *


class Day10Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(220, challenge1('day10.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(2244, challenge1('day10.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(19208, challenge2('day10.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(3947645370368, challenge2('day10.input'))


if __name__ == '__main__':
    unittest.main()
