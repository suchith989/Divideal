from user import *
from split import *


class Expense:
    __id = None
    __amount = None
    __paidBy = None
    __splits = []

    def __init__(self, amount, paidby, splits):
        self.__amount = amount
        self.__splits = splits
        self.__paidBy = paidby

    def setId(self, id):
        self.__id = id

    def setAmount(self, amount):
        self.__amount = amount

    def setPaidBy(self, paidby):
        self.__paidBy = paidby

    def setSplits(self, splits):
        self.__splits = splits

    def getId(self):
        return self.__id

    def getAmount(self):
        return self.__amount

    def getPaidBy(self):
        return self.__paidBy

    def getSplits(self):
        return self.__splits


class EqualExpense(Expense):

    def __init__(self, amount, paidby, splits):
        super().__init__(amount, paidby, splits)


class ExactExpense(Expense):

    def __init__(self, amount, paidby, splits):
        super().__init__(amount, paidby, splits)


class PercentExpense(Expense):

    def __init__(self, amount, paidby, splits):
        super().__init__(amount, paidby, splits)


class SharesExpense(Expense):

    def __init__(self, amount, paidby, splits):
        super().__init__(amount, paidby, splits)


class AdjustExpense(Expense):

    def __init__(self, amount, paidby, splits):
        super().__init__(amount, paidby, splits)
