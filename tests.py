import unittest
from Range import Range
from Range_generator import GenRange


class Test(unittest.TestCase):

    def test_positive_no_step(self):
        self.assertEqual(list(Range(3, 5)), list(range(3, 5)))

    def test_positive_step(self):
        self.assertEqual(list(Range(1, 5, 2)), list(range(1, 5, 2)))

    def test_negative(self):
        self.assertEqual(list(Range(-30, -5)), list(range(-30, -5)))

    def test_zero_step(self):
        with self.assertRaises(ValueError) as e:
            list(Range(1, 2, 0))
            raise ValueError(
                'This code must not be executed')

    def test_gen_positive_no_step(self):
        self.assertEqual(list(GenRange(3, 5)), list(range(3, 5)))

    def test_gen_positive_step(self):
        self.assertEqual(list(GenRange(1, 5, 2)), list(range(1, 5, 2)))

    def test_gen_negative(self):
        self.assertEqual(list(GenRange(-30, -5)), list(range(-30, -5)))

    def test_gen_zero_step(self):
        with self.assertRaises(ValueError) as e:
            list(GenRange(1, 2, 0))
            raise ValueError(
                'This code must not be executed')


if __name__ == '__main__':
    unittest.main()
