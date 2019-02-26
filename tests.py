import unittest
from Range_iterator import Range
from Range_generator import GenRange


class Test(unittest.TestCase):

    def test_positive_no_step(self):
        self.assertEqual(list(Range(3, 5)), list(range(3, 5)))

    def test_positive_step(self):
        self.assertEqual(list(Range(1, 5, 2)), list(range(1, 5, 2)))

    def test_negative(self):
        self.assertEqual(list(Range(-30, -5)), list(range(-30, -5)))

    def test_zero_step(self):
        self.assertRaises(ValueError, list(Range(1, 2, 0)))

    def test_gen_positive_no_step(self):
        self.assertEqual(list(GenRange(3, 5)), list(range(3, 5)))

    def test_gen_positive_step(self):
        self.assertEqual(list(GenRange(1, 5, 2)), list(range(1, 5, 2)))

    def test_gen_negative(self):
        self.assertEqual(list(GenRange(-30, -5)), list(range(-30, -5)))

    def test_gen_zero_step(self):
        self.assertRaises(ValueError, list(GenRange(1, 2, 0)))
