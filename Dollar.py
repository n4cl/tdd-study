# coding: utf-8


class Dollar(object):

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, obj):
        return self.amount == obj.amount
