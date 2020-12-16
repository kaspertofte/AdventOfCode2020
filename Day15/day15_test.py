import unittest
from Day15.day15 import *


class Day15Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(436, challenge1('day15.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(232, challenge1('day15.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(175594, challenge2('day15.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(18929178, challenge2('day15.input'))


if __name__ == '__main__':
    unittest.main()
