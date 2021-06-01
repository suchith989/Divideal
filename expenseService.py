from user import *
from split import *
from expense import *
from expenseType import *
from math import *


class ExpenseService:
    @staticmethod
    def createExpense(extype, amount, paidby, splits):
        if extype == expenseType[0]:
            return ExactExpense(amount, paidby, splits)

        elif extype == expenseType[1]:
            totalperamt = 0.0
            for split in splits:
                split.__class__ = PercentSplit
                percentvalue = float(round((amount * split.getPercent()) / 100.0, 2))
                totalperamt += percentvalue
                split.setAmount(percentvalue)
            splits[0].setAmount(round(splits[0].getAmount() - (totalperamt - amount), 2))
            return PercentExpense(amount, paidby, splits)

        elif extype == expenseType[2]:
            totalsplits = len(splits)
            splitamount = float(round(amount * 100 / totalsplits,2)) / 100.0
            for split in splits:
                split.setAmount(splitamount)
            splits[0].setAmount(splitamount + (amount - splitamount * totalsplits))
            return EqualExpense(amount, paidby, splits)

        elif extype == expenseType[3]:
            totalshares = 0.0
            totalshareamt = 0.0
            for split in splits:
                split.__class__ = SharesSplit
                totalshares += split.getShares()
            for split in splits:
                split.__class__ = SharesSplit
                sharevalue = float(round((amount * split.getShares()) / totalshares, 2))
                totalshareamt += sharevalue
                split.setAmount(sharevalue)
            splits[0].setAmount(round(splits[0].getAmount() - (totalshareamt - amount), 2))
            return SharesExpense(amount, paidby, splits)

        elif extype == expenseType[4]:
            for split in splits:
                split.__class__ = AdjustSplit
                amount -= split.getAdjust()

            totalsplits = len(splits)
            splitamount = float(round(amount * 100 / totalsplits, 2)) / 100.0
            for split in splits:
                split.setAmount(round(split.getAdjust() + splitamount, 2))
            splits[0].setAmount(round(splits[0].getAdjust() + splitamount + (amount - splitamount * totalsplits), 2))
            return AdjustExpense(amount, paidby, splits)

        else:
            return None
