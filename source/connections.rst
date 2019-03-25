Connections
=================

Creating a connection
#####################

Example::

   job = usr.addConnection(loginID="gavinBelson", password="hooli2016", institutionID="AU00000")
   
   if job.isComplete():
      connections = usr.getConnections()

   conn = connections[0] # Choose connection from list

Capabilities
######################

Detailed object methods and subroutines available `here <https://basiq-rapid.readthedocs.io/en/latest/objects.html#main.Connection>`_.

Basics
***********
Example usage::

   # Return ID
   conn.id
   # Return institution ID
   conn.institution_id
   # Return when last used
   conn.lastUsed
   # Return status (whether pending a job)
   conn.status

Refresh connection
*********************
Refresh connection to get latest transactions.

Example Usage::

   job = conn.refresh()

Get accounts
***************************
Returns a list of Account objects linked with connection.

Example Usage::

   accounts = conn.getAccounts()

Get transactions
***************************
Returns a list of Transaction objects linked with connection.

Example Usage::

   transactions = conn.getTransactions()
