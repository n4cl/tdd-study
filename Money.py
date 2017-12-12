# coding: utf-8


class Money(object):

    def __init__(self):
        # TODO: Pythonで基底クラスでのインスタンス変数の宣言をどうすれば良いのか
        # TODO: protectedが存在しないため、provateとする
        self._amount = 0

    def equals(self, obj):
        return self._amount == obj._amount

    def __eq__(self, other):
        # オブジェクトを比較した際には、このメソッドが呼ばれる
        return self._amount == other._amount
