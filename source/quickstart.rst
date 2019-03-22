Quickstart Guide
======================

**Import Basiq Rapid into Python**::

   import basiqrapid as bq

**Create a session**::

   API_KEY = ""

   session = bq.Session(API_KEY)

**Get institutions**::

   institution_dict = session.getInstitutions()
   wbc_code = institution_dict['Westpac Banking Corporation']

**Create a User**::

   usr = session.createUser(email="gavin@hooli.com", mobile="+61888000888")

**Create a connection**::

   job = usr.createConnection(loginID="gavinBelson", password="hooli2016", institutionID="AU00000")
   print(job.getStatus())

**Some User Capabilities**::

   transactions = usr.getTransactions() # Returns list of Transaction objects
   connections = usr.getConnections() # Returns list of Connection objects
   income = usr.getIncome()
   income_year = income.regularIncomeYear

**Some Connection Capabilities**::

   first_connection = connections[0]
   first_connection.institution_id # Returns institution ID
   accounts = first_connection.getAccounts()

**Some Account Capabilities**::
   
   first_account = accounts[0]
   transactions = first_account.getTransactions()

**Some Transaction Capabilities**::

   first_transaction = transactions[0]
   print(transaction.balance)
   print(transaction.description)

**Convert to pandas DataFrame**::

   import pandas as pd

   transactions = usr.getTransactions()
   trans_df = bq.to_df(transactions)

   accounts = usr.getAccounts()
   acc_df = bq.to_df(accounts)

**Filters**::

   f = bq.newFilter()
   f.gt("transaction.postDate","2018-01-28")
   transactions = usr.getTransactions(f)
