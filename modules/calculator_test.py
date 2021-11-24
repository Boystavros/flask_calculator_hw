import unittest
from modules.calculator import *


class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        result = add(1, 1)
        self.assertEqual(2, result)

    def test_subtract(self):
        result = subtract(2, 1)
        self.assertEqual(1, result)

    def test_multiply(self):
        result = multiply(2, 3)
        self.assertEqual(6, result)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(5, result)
