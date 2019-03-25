Transactions
=================

Creating a transaction
#####################

Use .getTransaction() method on User, Connection, or Account objects.

Example::

   accounts = usr.getAccounts()
   acc = accounts[1]

Capabilities
######################

Detailed object methods and subroutines available `here <https://basiq-rapid.readthedocs.io/en/latest/objects.html#main.Connection>`_.

Basics
***********
Example usage::

   # Return ANZSIC code
   trans.ANZSIC_code

   # Return ANZSIC title
   trans.ANZSIC_title

   # Return parent account ID
   trans.account

   # Return transaction amount
   trans.amount

   # Return balance after transaction
   trans.balance

   # Return parent connection ID
   trans.connection

   # Return transaction description
   trans.description

   # Return direction of transaction (eg. credit)
   trans.direction

   # Return transaction ID
   trans.id

   # Return parent institution ID
   trans.institution

   # Return transaction post date
   trans.postDate

   # Return transaction status (eg. posted)
   trans.status

   # Return transaction date (empty if not complete)
   trans.transactionDate
