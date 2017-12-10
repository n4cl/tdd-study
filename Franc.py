# coding: utf-8


class Franc(object):

    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)

    def equals(self, obj):
        return self.__amount == obj.__amount

    def __eq__(self, other):
        # オブジェクトを比較した際には、このメソッドが呼ばれる
        return self.__amount == other.__amount
