# coding: utf-8

import unittest
from Dollar import Dollar


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))


if __name__ == "__main__":
    unittest.main()
