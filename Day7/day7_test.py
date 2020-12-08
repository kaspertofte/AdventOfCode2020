import unittest
from Day7.day7 import *


class Day7Test(unittest.TestCase):
    def test_challenge1_on_test_data(self):
        self.assertEqual(4, challenge1('day7.test'))

    def test_challenge1_on_real_data(self):
        self.assertEqual(222, challenge1('day7.input'))

    def test_challenge2_on_test_data(self):
        self.assertEqual(32, challenge2('day7.test'))

    def test_challenge2_on_real_data(self):
        self.assertEqual(13264, challenge2('day7.input'))


if __name__ == '__main__':
    unittest.main()
