"""Unit tests for the Calculator class.

Run with:  python -m pytest
       or  python -m unittest discover tests
"""

import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # --- add ---

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_decimals(self):
        self.assertAlmostEqual(self.calc.add(1.5, 2.25), 3.75)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(7, 0), 7)

    # --- subtract ---

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_to_negative(self):
        self.assertEqual(self.calc.subtract(3, 8), -5)

    def test_subtract_decimals(self):
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.25), 1.25)

    # --- multiply ---

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(99, 0), 0)

    def test_multiply_negatives(self):
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_decimals(self):
        self.assertAlmostEqual(self.calc.multiply(1.5, 4), 6.0)

    # --- divide ---

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_divide_to_whole_number(self):
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
