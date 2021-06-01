from user import *
from split import *
from expense import *
from expenseType import *
from expenseService import *
from edit_participants import *
import sqlite3

class ExpenseManager:
    expenses = None
    userMap = None
    balanceSheet = None

    def __init__(self):
        self.expenses = []
        self.userMap = {}
        self.balanceSheet = {}

    def addUser(self, user):
        self.userMap.__setitem__(user.getId(), user)
        self.balanceSheet.__setitem__(user.getId(), {})

    def addExpense(self, extype, amount, paidby, splits):
        # db_table = database_entry()
        # db_table.edit_entry(paidby,amount,"ADD",potid,conn)
        transaction_details = []
        transaction_details.append(("ADD",paidby,amount))
        paidbydict = self.userMap.get(paidby)
        expense = ExpenseService.createExpense(extype, amount, paidbydict, splits)
        self.expenses.append(expense)
        for split in expense.getSplits():
            paidto = split.getUser().getId()
            # db_table.edit_entry(paidto,split.getAmount(),"DEDUCT",potid,conn)
            transaction_details.append(("DEDUCT",paidto,split.getAmount()))
            balances = self.balanceSheet.get(paidby)
            if paidto not in balances:
                balances[paidto] = 0.0

            balances[paidto] = balances.get(paidto) + split.getAmount()
            self.balanceSheet.__setitem__(paidby, balances)

            balances = self.balanceSheet.get(paidto)
            if paidby not in balances:
                balances[paidby] = 0.0

            balances[paidby] = balances.get(paidby) - split.getAmount()
            self.balanceSheet.__setitem__(paidto, balances)

        return transaction_details
        

    def showBalances(self):
        if not bool(self.balanceSheet):
            print("No Balances")
        else:
            print(self.balanceSheet)
