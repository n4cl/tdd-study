# coding: utf-8

from Money import Money


class Dollar(Money):

    def __init__(self, amount):
        super(Dollar, self).__init__()
        self._amount = amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)
