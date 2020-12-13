import unittest
from Day13.day13 import *


class Day13Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(295, challenge1('day13.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(259, challenge1('day13.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(1068781, challenge2('day13.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(210612924879242, challenge2('day13.input'))


if __name__ == '__main__':
    unittest.main()
