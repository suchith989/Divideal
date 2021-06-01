from user import *


class Split:
    _user = None  # user is of User type object
    amount = None

    def __init__(self, user):
        self._user = user

    def setUser(self, user):
        self._user = user

    def setAmount(self, amount):
        self.amount = amount

    def getUser(self):
        return self._user

    def getAmount(self):
        return self.amount


class EqualSplit(Split):
    def __init__(self, user):
        super().__init__(user)


class ExactSplit(Split):
    def __init__(self, user, amount):
        super().__init__(user)
        self.amount = amount


class PercentSplit(Split):
    percent = None

    def __init__(self, user, percent):
        super().__init__(user)
        self.percent = percent

    def setPercent(self, percent):
        self.percent = percent

    def getPercent(self):
        return self.percent


class SharesSplit(Split):
    share = None

    def __init__(self, user, share):
        super().__init__(user)
        self.share = share

    def setShares(self, share):
        self.share = share

    def getShares(self):
        return self.share


class AdjustSplit(Split):
    adjust = None

    def __init__(self, user, adjust):
        super().__init__(user)
        self.adjust = adjust

    def setAdjust(self, adjust):
        self.adjust = adjust

    def getAdjust(self):
        return self.adjust
