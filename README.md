# Divideal
App to split your expenses and simplify them to their minimum number of transactions possible.

CLI python app takes the user input and calculates the total debts each person in the group have. 
At the end we run Ford-fulkerson or a simple greedy approach to reduce the no. of transactions to their minimum.

Input for CLI:

<EXPENSE/SHOW> <Type of split> <Payee> <Amount> <No.of users> <Users involved> <Amounts/Values>
  
We can make 5 different kinds of splits 
  * EQUAL
  * EXACT
  * SHARES
  * PERCENT
  * ADJUST

You can access the same app from our flask app at [DiviDeal](https://divideal.pythonanywhere.com)

