Filters
=================

Creating a filter
#####################

Example::

   f = bq.newFilter()

Options
##########

Filters are used in accordance with the Basiq API's capabilities.

Filter objects can have any amount of conditionals:
- equal to (eq)
- between (bt)
- greater than (gt)
- greater than or equal to (gteq)
- less than (lt)
- less than or equal to (lteq)

Equal to (eq)
******************

Example::

   f.eq("account.id","s55bf3")

Between (bt)
***************

Values are inclusive

Example::

   f.bt("transaction.postDate","2017-09-28","2018-01-30")

Greater than (gt)
*********************

Example::

   f.gt("transaction.postDate","2017-09-28")

Greater than or equal to (gteq)
**********************************

Example::

   f.gteq("transaction.postDate","2017-09-28")

Less than (lt)
****************

Example::

   f.lt("transaction.postDate","2017-09-28")

Less than or equal to (lteq)
****************

Example::

   f.lteq("transaction.postDate","2017-09-28")

Usage
###########

Add to any get methods.

Example usage::

   # Passed as parameter to getAccounts method
   accounts = usr.getAccounts(f)


