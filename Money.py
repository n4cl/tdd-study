# coding: utf-8

from abc import ABCMeta, abstractmethod


class Money(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        # TODO: Pythonで基底クラスでのインスタンス変数の宣言をどうすれば良いのか
        # TODO: protectedが存在しないため、provateとする
        self._amount = 0

    @abstractmethod
    def times(self, multiplier):
        pass

    def equals(self, obj):
        return (self._amount   == obj._amount
            and self.__class__ == obj.__class__)

    def __eq__(self, other):
        # オブジェクトを比較した際には、このメソッドが呼ばれる
        return (self._amount   == other._amount
           and  self.__class__ == other.__class__)

    @staticmethod
    def dollar(amount):
        from Dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        from Franc import Franc
        return Franc(amount)
