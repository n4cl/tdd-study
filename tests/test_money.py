# coding: utf-8

import unittest
from Money import Money
from Franc import Franc


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5).equals(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).equals(Money.dollar(6)))
        self.assertTrue(Franc(5).equals(Franc(5)))
        self.assertFalse(Franc(5).equals(Franc(6)))
        self.assertFalse(Money.dollar(5).equals(Franc(5)))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

if __name__ == "__main__":
    unittest.main()
