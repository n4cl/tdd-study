# coding: utf-8

from Money import Money


class Franc(Money):

    def __init__(self, amount):
        super(Franc, self).__init__()
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)
