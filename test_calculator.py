#generate tests for Calculator class
"""
Tests for Calculator class.

Author: [Your Name]
Date: [Today's Date]

"""

import unittest
from calculator import Calculator  # <--- Import the Calculator class

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -4), -6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 7), 3)
        self.assertEqual(self.calc.subtract(4, 6), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-2, -4), 8)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.33333333)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)  # Test division by zero error

    def test_sqrt(self):
        self.assertAlmostEqual(self.calc.square_root(4), 2)
        self.assertAlmostEqual(self.calc.square_root(16), 4)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)  # Test sqrt of negative number error

    def test_power(self):
        self.assertEqual(self.calc.power(5, 3), 125)
        self.assertEqual(self.calc.power(2, 0), 1)
        self.assertEqual(self.calc.power(-4, -1), -0.25)

if __name__ == '__main__':
    unittest.main()
