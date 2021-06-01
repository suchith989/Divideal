# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# EXPENSE U6 5000 2 U3 U6 PERCENT 50 50
# EXPENSE U4 2000 3 U1 U2 U3 ADJUST 2000 0 0

from user import *
from split import *
from expense import *
from expenseType import *
from expenseService import *
from expenseManager import *
# from simplify import *
from simplify2 import *
import os
import json
from balance_sheet import *
from pots import *
from edit_participants import *
from transactions import *



def add_User_db(pot_id):
    name = input("Enter the name of the user")
    email = input("Enter the mail id ")
    db_participant = database_entry()
    user_id = db_participant.add_single_participant(pot_id,name,email)
    expenseManager.addUser(User(user_id, name, email))

def get_user_db(pot_id):
    db_participant = database_entry()
    users = db_participant.get_every_participant(pot_id)
    for user in users:
        expenseManager.addUser(User(user[0],user[1],user[2]))


if __name__ == '__main__':
    expenseManager = ExpenseManager()
    db_balance_sheet = balancesheet()
    db_pot = pots()
    db_transact = transact()
    pot_id = 0
    db_participant = database_entry()

    # expenseManager.addUser(User("U1", "User1", "gaurav@workat.tech"))
    # expenseManager.addUser(User("U2", "User2", "sagar@workat.tech"))
    # expenseManager.addUser(User("U3", "User3", "hi@workat.tech"))
    # expenseManager.addUser(User("U4", "User4", "mock-interviews@workat.tech"))
    # expenseManager.addUser(User("U5", "User5", "abc@gmail.com"))
    # expenseManager.addUser(User("U6", "User6", "hihello@yahoo.in"))
    # expenseManager.addUser(User("U7", "User7", "hi@workat.tech"))
    # expenseManager.addUser(User("U8", "User8", "mock-interviews@workat.tech"))
    # expenseManager.addUser(User("U9", "User9", "abc@gmail.com"))
    # expenseManager.addUser(User("U10", "User10", "hihello@yahoo.in"))


    if input("Enter OPEN or NEW: ") == "OPEN":
        pots = db_pot.get_pots() #READ
        if len(pots) == 0:
            print("No pots exist- Create new pot-Enter new pot name")
            expense_name = input("Enter a new pot name: ")
            new = 1
                
            db_pot.set_pot(expense_name, "3480290sheiefiuv") #UPDATE
            pot_id = db_pot.get_potid(expense_name) #READ
            participant_entry = database_entry()
            participant_entry.add_every_participant(pot_id[0],expenseManager.userMap) #UPDATE
            pot_id = pot_id[0]
            while int(input("Do you want to add another User (1/0) ?")):
                add_User_db(pot_id)
        else:
            new = 0
            print(pots)
            pot_id = int(input("Give id of pot"))
            get_user_db(pot_id)
            balancesheet = db_pot.getbalance(pot_id) #READ
            expenseManager.balanceSheet = balancesheet
        
    else:
        expense_name = input("Enter a new pot name: ")
        new = 1
       

        db_pot.set_pot(expense_name, "3480290sheiefiuv",connection) #UPDATE
        pot_id = db_pot.get_potid(expense_name,connection) #READ
        participant_entry = database_entry()
        participant_entry.add_every_participant(pot_id[0],connection,expenseManager.userMap) #UPDATE
        pot_id = pot_id[0]
        while int(input("Do you want to add another User (1/0) ?")):
            add_User_db(pot_id)

    while 1:
        commands = input().split()
        commandType = commands[0]

        if commandType == "SHOW":
            expenseManager.showBalances()
        elif commandType == "SIMPLIFY":
            expenseManager.balanceSheet = simplify.simplify(expenseManager.balanceSheet)
            db_balance_sheet.update_balance_sheet(expenseManager.balanceSheet,pot_id)
        elif commandType == "EXPENSE":
            paidby = commands[1]
            amount = float(commands[2])
            noOfUsers = int(commands[3])
            expensetype = commands[4 + noOfUsers]
            splits = []

            if expensetype == "EQUAL":
                for i in range(noOfUsers):
                    splits.append(EqualSplit(expenseManager.userMap.get(commands[4 + i])))
                details = expenseManager.addExpense(expenseType[2], amount, paidby, splits)

            elif expensetype == "EXACT":
                for i in range(noOfUsers):
                    splits.append(ExactSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                details = expenseManager.addExpense(expenseType[0], amount, paidby, splits)

            elif expensetype == "PERCENT":
                for i in range(noOfUsers):
                    splits.append(PercentSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                details = expenseManager.addExpense(expenseType[1], amount, paidby, splits)

            elif expensetype == "SHARES":
                for i in range(noOfUsers):
                    splits.append(SharesSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                details = expenseManager.addExpense(expenseType[3], amount, paidby, splits)

            elif expensetype == "ADJUST":
                for i in range(noOfUsers):
                    splits.append(AdjustSplit(expenseManager.userMap.get(commands[4+i]), float(commands[5+noOfUsers+i])))
                details = expenseManager.addExpense(expenseType[4], amount, paidby, splits)
            
            description = input("Give a description for transaction")
            db_transact.update_items(details,description,pot_id)
            
            for single_trans in details:
                db_participant.edit_entry(single_trans,pot_id) #DONE editing
            db_balance_sheet.update_balance_sheet(expenseManager.balanceSheet,pot_id)
        else:
            break

       