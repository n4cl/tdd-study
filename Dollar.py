# coding: utf-8


class Dollar(object):

    amount = 0

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier
