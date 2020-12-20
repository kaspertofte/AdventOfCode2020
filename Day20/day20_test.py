import unittest
from Day20.day20 import *


class Day20Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(0, challenge1('day20.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(0, challenge1('day20.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(0, challenge2('day20.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(0, challenge2('day20.input'))


if __name__ == '__main__':
    unittest.main()
