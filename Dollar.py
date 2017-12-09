# coding: utf-8


class Dollar(object):

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, obj):
        return self.amount == obj.amount

    def __eq__(self, other):
        # オブジェクトを比較した際には、このメソッドが呼ばれる
        return self.amount == other.amount
