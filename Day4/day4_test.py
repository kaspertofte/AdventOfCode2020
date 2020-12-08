import unittest
from Day4.day4 import *


class Day4Test(unittest.TestCase):
    def test_byr_validator(self):
        self.assertTrue(byrValidator('2002'))

    def test_num_valid_passports_on_input(self):
        self.assertEqual(numValidPassports('day4.input'), 127)

    def test_num_valid_passports_on_testt(self):
        self.assertEqual(numValidPassports('day4.test'), 2)


if __name__ == '__main__':
    unittest.main()
