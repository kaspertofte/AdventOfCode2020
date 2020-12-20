import unittest
from Day19.day19 import *


class Day19Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(0, challenge1('day19.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(0, challenge1('day19.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(0, challenge2('day19.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(0, challenge2('day19.input'))


if __name__ == '__main__':
    unittest.main()
