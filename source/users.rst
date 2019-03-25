Users
=================

Creating a user
#####################

Creating a user::

   usr = session.createUser(email="gavinBelson",mobile="+61888000888")

Or::

   user_id = "88888888"
   usr = session.getUser(user_id)

Capabilities
######################

Detailed object methods and subroutines available `here <https://basiq-rapid.readthedocs.io/en/latest/objects.html#main.User>`_.

Basics
***********
Example usage::

   # Return email
   usr.email
   # Return mobile
   usr.mobile
   # Return ID
   usr.id

Update user details
*********************
Example Usage::

   usr.update(email="new@email.com", mobile="+61409838099")
   # Returns True if success

Get transactions
***************************
Returns a list of Transaction objects.

Example Usage::

   transactions = usr.getTransactions()

Get income
*************************
Returns an Income object.

Example Usage::

   income = usr.getIncome()
   print(income.regularIncomeYear)

Get Expenses
*********************************
Returns an Expense object.

Example Usage::

   expense = usr.getExpenses()
   print(expense.totalMonthly)

Add Connection
***************
Returns a Job object

Example Usage::

   job = usr.addConnection(loginID="gavinBelson", password="hooli2016", institutionID="AU00000")

Get Accounts
****************
Returns list of Account objects.

Example Usage::

   accounts = usr.getAccounts()

Get Connections
****************
Returns list of Connection objects.

Example Usage::

   connections = usr.getConnections()
